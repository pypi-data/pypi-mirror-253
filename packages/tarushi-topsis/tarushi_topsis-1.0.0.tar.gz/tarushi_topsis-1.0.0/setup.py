import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tarushi_topsis",
    version="1.0.0",
    description="Topsis - multiple criteria decision making",
    long_description_content_type="text/markdown",
    url="https://github.com/tarushirastogi/tarushi-topsis",
    author="Tarushi Rastogi",
    author_email="tarushirastogi04@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[],
    
)