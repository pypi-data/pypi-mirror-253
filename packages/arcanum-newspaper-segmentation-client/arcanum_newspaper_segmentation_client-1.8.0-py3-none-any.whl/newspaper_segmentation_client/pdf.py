from PIL import Image
import fitz

from newspaper_segmentation_client import run_newspaper_segmentation_on_image


def render_pdf_page(page: fitz.Page, dpi: int = 150) -> Image:
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    pix = page.get_pixmap(matrix=mat, annots=False, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def run_newspaper_segmentation_on_pdf_page(page: fitz.Page, api_key: str):
    image = render_pdf_page(page)
    return run_newspaper_segmentation_on_image(image, api_key)
