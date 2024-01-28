import importlib.util
import sys
import string
import secrets
import json
import os
import gc
import torch
import time
import datetime
from PIL import Image
from base64 import b64decode
from io import BytesIO
from os import path
import socket
from contextlib import closing

from flask import send_file
from .setting import output_path, is_mac, aiapps_path


def get_nowstr():
    return datetime.now().strftime("%Y%m%d%H%M%S")


class timer:
    def __init__(self, method_name="timed process"):
        self.method = method_name

    def __enter__(self):
        self.start = time.time()
        print(f"{self.method} starts")

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"{self.method} took {str(round(end - self.start, 2))}s")


def dataurl_to_image(data_url):
    _, encoded = data_url.split("base64,")
    data = b64decode(encoded)
    o = BytesIO(data)
    m = Image.open(o)
    return m


def serve_pil_image(pil_img: Image.Image):
    img_io = BytesIO()
    pil_img.save(img_io, "png", quality=70)
    img_io.seek(0)
    pil_img.save(path.join(output_path, get_nowstr() + ".png"))
    return send_file(img_io, mimetype="image/png")


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("localhost", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def clear_memory():
    global infer
    if infer.get("pipe"):
        del infer["pipe"]
    gc.collect()
    if not is_mac and torch.cuda.is_available():
        torch.cuda.empty_cache()
    if is_mac:
        torch.mps.empty_cache()


def parse_port(raw):
    # Example: ###PORT:12345
    return raw.split(":")[1]


def check_model_files_exist(app_name, app_info):
    if not app_info.get("models"):
        return True
    # TODO
    return True


def load_aiapps_json():
    aiapps = []
    for filename in os.listdir(aiapps_path):
        if os.path.isdir(os.path.join(aiapps_path, filename)):
            aiapps.append(
                {
                    "name": filename,
                    "info": json.load(
                        open(
                            os.path.join(aiapps_path, filename, "app.json"),
                            "r",
                            encoding="utf-8",
                        )
                    ),
                }
            )
    return aiapps
