from setuptools import setup, find_packages

setup(
    name = 'haji-api',
    version = '0.0.1',
    author= 'Erfan Bafandeh',
    author_email = 'user.enbh@gmail.com',
    description = 'haji api has best web services.',
    keywords = ['web-service', 'api', 'haji-api'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.6",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Erfan-Bafandeh/haji-api',
    packages = find_packages(),
    install_requires = ["requests"],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ]
)
