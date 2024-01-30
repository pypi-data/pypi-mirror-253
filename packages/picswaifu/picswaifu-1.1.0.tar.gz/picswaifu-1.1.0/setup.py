from setuptools import setup

setup(
    name='picswaifu',
    packages=["picswaifu"],
    version='1.1.0',
    long_description="""# Python Waifu Pics API Client

WaifuPics is a Python client for the Waifu Pics API, providing a simple and convenient way to retrieve SFW and NSFW images of various categories.

## Installation

You can install WaifuPics using pip:

```sh
pip install picswaifu
```

# Usage

```py
from picswaifu import Waifu, ApiTypes, SFWCats, NSFWCats

# Create an instance of WaifuPics

waifu_client = Waifu()

# Get a single SFW image URL
sfw_url = await waifu_client.get()
print(f"SFW Image URL: {sfw_url}")

# Get multiple SFW images URLs as a list
sfw_urls = await waifu_client.get_sfw(category=SFWCats.NEKO, multi=True)
for url in sfw_urls:
    print(f"SFW Image URL: {url}")
```

# Errors

- InvalidResponse: Raised when the API returns an invalid response.
- InvalidInput: Raised when the client is not configured properly.

# Notes
This package uses the Waifu Pics API. Make sure to review and comply with the API's terms of service.

# Contributing

Feel free to contribute by opening issues or submitting pull requests on the GitHub repository.

# License
This project is licensed under the GPLv3 License - see the LICENSE file for details.
""",
    long_description_content_type='text/markdown',
    author='fswair',
    url="https://gist.github.com/fswair/d1306ae27e13fa90210b3f16832ec218",
    install_requires=[
        'aiohttp',
    ],
    python_requires='>=3.8',
)