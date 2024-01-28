from setuptools import find_packages, setup

setup(
    name="mlv",
    version="1.1.0",
    install_requires=["requests[socks]==2.31.*", "flask==3.0.*", "huggingface-hub"],
    packages=find_packages("mlv"),
    python_requires=">=3.10",
)
