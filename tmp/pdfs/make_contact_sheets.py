from pathlib import Path
import sys

from PIL import Image, ImageDraw
import pypdfium2 as pdfium


source = Path(sys.argv[1])
output_dir = Path(sys.argv[2])
pages = [int(value) for value in sys.argv[3:]]
output_dir.mkdir(parents=True, exist_ok=True)
document = pdfium.PdfDocument(str(source))

thumb_w, thumb_h = 340, 460
cell_w, cell_h = 360, 500
columns, rows = 4, 4
for sheet_index in range(0, len(pages), columns * rows):
    batch = pages[sheet_index:sheet_index + columns * rows]
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    for index, number in enumerate(batch):
        image = document[number - 1].render(scale=0.75).to_pil().convert("RGB")
        image.thumbnail((thumb_w, thumb_h))
        x = (index % columns) * cell_w + (cell_w - image.width) // 2
        y = (index // columns) * cell_h + 28
        sheet.paste(image, (x, y))
        draw.text((index % columns * cell_w + 8, index // columns * cell_h + 5), f"Página {number}", fill="black")
    target = output_dir / f"contact-{sheet_index // (columns * rows) + 1:02d}.jpg"
    sheet.save(target, quality=88)
    print(target.resolve())
