import json
import io
import base64
from typing import BinaryIO

import requests
from PIL import Image


def run_newspaper_segmentation_on_image(image: Image, api_key: str) -> dict:
    image_width = image.width
    image.thumbnail((2000, 2000))
    scale = image.width / image_width
    request_data = {}

    with io.BytesIO() as image_io:
        image.save(image_io, "JPEG", quality=60)
        request_data["image_base64"] = base64.b64encode(image_io.getvalue()).decode("ascii")
        request_data["dpi"] = 150 * scale

    response = requests.get("https://api.arcanum.com/v1/newspaper-segmentation/analyze-page",
                            data=json.dumps(request_data), headers={"x-api-key": api_key})
    return response.json()


def run_newspaper_segmentation(image: BinaryIO, api_key: str):
    image_bytes = Image.open(image)
    return run_newspaper_segmentation_on_image(image_bytes, api_key)
