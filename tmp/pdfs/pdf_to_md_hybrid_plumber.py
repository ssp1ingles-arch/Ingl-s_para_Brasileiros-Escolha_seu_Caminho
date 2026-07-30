from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import numpy as np
import pdfplumber
import pypdfium2 as pdfium
from rapidocr_onnxruntime import RapidOCR


def clean_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.replace("\u00ad", "").replace("\u00a0", " ").splitlines():
        raw = re.sub(r"\(cid:\d+\)", " ", raw)
        line = re.sub(r"[ \t]+", " ", raw).strip()
        if line:
            lines.append(line)
    return lines


def ocr_page(doc: pdfium.PdfDocument, engine: RapidOCR, index: int, scale: float) -> tuple[list[str], float]:
    image = np.asarray(doc[index].render(scale=scale).to_pil())
    result, _ = engine(image)
    lines: list[str] = []
    scores: list[float] = []
    for item in result or []:
        line = re.sub(r"[ \t]+", " ", str(item[1]).replace("\u00ad", "").replace("\u00a0", " ")).strip()
        if line:
            lines.append(line)
            scores.append(float(item[2]))
    return lines, (sum(scores) / len(scores) if scores else 0.0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--ocr-threshold", type=int, default=40)
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--checkpoint-dir", type=Path, default=Path("tmp/pdfs/checkpoints"))
    args = parser.parse_args()

    source = args.input.resolve()
    destination = args.output.resolve()
    checkpoint_dir = args.checkpoint_dir.resolve()
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", source.stem).strip("_")
    checkpoint = checkpoint_dir / f"{safe_name}_{source.stat().st_size}.jsonl"
    render_doc = pdfium.PdfDocument(str(source))
    engine: RapidOCR | None = None
    page_map: dict[int, tuple[int, list[str], str, float]] = {}
    if checkpoint.exists():
        for raw in checkpoint.read_text(encoding="utf-8").splitlines():
            try:
                saved = json.loads(raw)
                number = int(saved["number"])
                page_map[number] = (number, list(saved["lines"]), str(saved["method"]), float(saved["confidence"]))
            except (ValueError, KeyError, TypeError, json.JSONDecodeError):
                continue
        if page_map:
            print(f"Retomando checkpoint: {len(page_map)} páginas já processadas.", flush=True)
    started = time.time()

    with pdfplumber.open(source) as document:
        total = len(document.pages)
        for index, page in enumerate(document.pages):
            number = index + 1
            if number in page_map:
                _, saved_lines, saved_method, saved_confidence = page_map[number]
                print(f"[{number:03d}/{total}] retomada: {len(saved_lines):03d} linhas ({saved_method})", flush=True)
                continue
            try:
                extracted = page.extract_text(x_tolerance=2, y_tolerance=3, layout=True) or ""
            except Exception:
                extracted = ""
            extracted_lines = clean_lines(extracted)
            suspicious = any(len(line) > 500 for line in extracted_lines)
            method = "texto"
            confidence = 1.0
            if len(extracted.strip()) < args.ocr_threshold or suspicious or "\ufffd" in extracted:
                if engine is None:
                    engine = RapidOCR()
                lines, confidence = ocr_page(render_doc, engine, index, args.scale)
                method = "OCR"
            else:
                lines = extracted_lines
            record = (number, lines, method, confidence)
            page_map[number] = record
            with checkpoint.open("a", encoding="utf-8", newline="\n") as cache:
                cache.write(json.dumps({"number": number, "lines": lines, "method": method, "confidence": confidence}, ensure_ascii=False) + "\n")
                cache.flush()
                os.fsync(cache.fileno())
            print(
                f"[{number:03d}/{total}] {method}: {len(lines):03d} linhas"
                + (f", confiança {confidence:.3f}" if method == "OCR" and lines else ""),
                flush=True,
            )

    pages = [page_map[number] for number in range(1, len(render_doc) + 1)]
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(f"# {source.stem}\n")
        written = False
        for number, lines, _, _ in pages:
            if not lines:
                continue
            if written:
                stream.write("\n---\n")
            stream.write(f"\n## Página {number}\n\n")
            stream.write("\n".join(lines))
            stream.write("\n")
            written = True

    textual = sum(bool(lines) for _, lines, _, _ in pages)
    ocr_pages = [number for number, _, method, _ in pages if method == "OCR"]
    low_conf = [number for number, lines, method, score in pages if lines and method == "OCR" and score < 0.85]
    print(
        f"Concluído em {time.time() - started:.1f}s: {len(pages)} páginas analisadas; "
        f"{textual} com texto; OCR={ocr_pages}; baixa confiança={low_conf}",
        flush=True,
    )
    checkpoint.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
