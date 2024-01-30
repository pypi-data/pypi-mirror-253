from setuptools import setup

version = "0.0.1"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

description = """
    vapeuniverse module microservice models
"""

setup(
    name="vape_models",
    version=version,

    author="nChurn",
    author_email="wapeuniverse@gmail.com",

    description=description,
    long_description=long_description,
    url="https://github.com/vapeuniverse/vape_models",
    download_url="https://github.com/vapeuniverse/vape_clients/archive/{}.zip".format(version),

    packages=["vape_models"],
    install_requires=[
        "pydantic"
    ]
)