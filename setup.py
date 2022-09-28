import pathlib
from setuptools import setup
from setuptools import find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="jd-sdk",
    version="1.0.3",
    packages=["jd", "api", "security"],
    package_dir={
        "": ".",
        "api": "jd/api",
        "security": "jd/security",
    },
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
    install_requires=["rsa", "psutil", "apscheduler", "wincertstore"],
    python_requires = '>=3.6',
)
