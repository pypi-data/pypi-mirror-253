from setuptools import setup, find_packages

setup(
    name="pycleancodecli",
    version="0.1",
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
    long_description="A tool to clean Python code files from comments and unnecessary whitespace.",
    long_description_content_type="text/markdown",
    url="https://github.com/ken1009us/pycleancodecli",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
