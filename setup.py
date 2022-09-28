import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="jd-sdk",
    version="1.1.1",
    packages=find_packages(),
    description="JD Official SDK",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PsKs/jd-sdk",
    author="Pongsakorn",
    author_email="pongsakorn.psks@gmail.com",
    license="LICENSE.md",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["rsa", "psutil", "apscheduler", "wincertstore", "pycryptodome"],
    python_requires='>=3.6',
)
