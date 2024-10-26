"""Define the setup."""

from pathlib import Path

import setuptools

with Path("README.md").open() as fh:
    long_description = fh.read()

setuptools.setup(
    name="creality_wifi_box_client",
    version="0.0.1",
    author="Patrick Cartwright",
    author_email="pcartwright1981@gmail.com",
    description="Client for Creality Wifi Box",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pcartwright81/creality_wifi_box_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
