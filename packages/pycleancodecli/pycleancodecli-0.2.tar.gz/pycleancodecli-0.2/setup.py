from setuptools import setup, find_packages

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pycleancodecli",
    version="0.2",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pycleancodecli=pycleancodecli.main:main",
        ],
    },
    author="Ken Wu",
    author_email="kenwu1009us@gmail.com",
    description="A tool to clean comment-out code in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ken1009us/pycleancodecli",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
