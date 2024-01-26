import json
import io
import base64
from typing import BinaryIO

import requests
from PIL import Image


def get_request_data(image: Image, dpi: int = 150, max_size: int = 2000, jpeg_quality: int = 60) \
        -> dict:
    image_width = image.width
    image.thumbnail((max_size, max_size))
    scale = image.width / image_width
    request_data = {}

    with io.BytesIO() as image_io:
        image.save(image_io, "JPEG", quality=jpeg_quality)
        request_data["image_base64"] = base64.b64encode(image_io.getvalue()).decode("ascii")
        request_data["dpi"] = dpi * scale
    return request_data


def run_newspaper_segmentation_on_image(image: Image, api_key: str, dpi: int = 150,
                                        max_size: int = 2000, jpeg_quality: int = 60) \
        -> dict:
    request_data = get_request_data(image, dpi, max_size, jpeg_quality)

    response = requests.get("https://api.arcanum.com/v1/newspaper-segmentation/analyze-page",
                            data=json.dumps(request_data), headers={"x-api-key": api_key})
    return response.json()


def run_newspaper_segmentation(image: BinaryIO, api_key: str, dpi: int = 150):
    image_bytes = Image.open(image)
    return run_newspaper_segmentation_on_image(image_bytes, api_key, dpi=dpi)
