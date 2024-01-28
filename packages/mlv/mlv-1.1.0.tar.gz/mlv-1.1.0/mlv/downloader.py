import os
import requests
from huggingface_hub import hf_hub_url
from mlv.setting import proxies


class DownloadManager:
    def __init__(self, base_model_path) -> None:
        self.base_model_path = base_model_path

    def from_huggingface(self, repo_id, filename, subfolder=None):
        # Don't use hf_hub_download here, beacause no progess handler
        # hf_hub_download(repo_id=repo_id, filename=filename, local_dir=cache_path)
        url = hf_hub_url(repo_id=repo_id, filename=filename, subfolder=subfolder)
        yield from self.from_url(url, filename)

    def from_url(self, url, save_filename):
        try:
            print("Start download from url: ", url)
            response = requests.get(url, stream=True, timeout=300, proxies=proxies)
            total_size_in_bytes = int(response.headers.get("content-length", 0))
            block_size = 1024 * 1024  # 1 Kibibyte * 1024 = 1MB
            downloaded_size = 0
            if total_size_in_bytes == 0:
                yield b"end"
            else:
                with open(
                    os.path.join(self.base_model_path, save_filename), "wb"
                ) as fp:
                    for data in response.iter_content(block_size):
                        fp.write(data)
                        downloaded_size += len(data)
                        yield str(downloaded_size / total_size_in_bytes).encode("utf-8")
                yield b"end"
        except Exception as e:
            print(e)
            yield b"error"
