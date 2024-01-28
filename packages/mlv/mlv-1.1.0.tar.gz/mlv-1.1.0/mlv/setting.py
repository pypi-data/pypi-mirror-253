import os
from os import path
from sys import platform

import mlv.mps_workaround

base_path = os.getenv("BASE_PATH")
cache_path = path.join(base_path, "models")
output_path = path.join(base_path, "output")
aiapps_path = path.join(os.getenv("INSALLANYAI_ROOT") or ".", "aiapps")
proxies = {"https": os.getenv("https_proxy")}
os.environ["TRANSFORMERS_CACHE"] = cache_path
os.environ["HF_HUB_CACHE"] = cache_path
os.environ["HF_HOME"] = cache_path
print("Base Path is: ", base_path)
print("Cache Path is: ", cache_path)
print("Output Path is: ", output_path)
is_mac = platform == "darwin"
