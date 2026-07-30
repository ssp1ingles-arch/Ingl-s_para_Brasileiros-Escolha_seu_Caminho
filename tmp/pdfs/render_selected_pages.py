from pathlib import Path
import sys

import pypdfium2 as pdfium


source = Path(sys.argv[1])
output_dir = Path(sys.argv[2])
pages = [int(value) for value in sys.argv[3:]]
output_dir.mkdir(parents=True, exist_ok=True)

document = pdfium.PdfDocument(str(source))
for number in pages:
    image = document[number - 1].render(scale=4.0).to_pil()
    target = output_dir / f"page-{number:03d}.png"
    image.save(target)
    print(target.resolve())
