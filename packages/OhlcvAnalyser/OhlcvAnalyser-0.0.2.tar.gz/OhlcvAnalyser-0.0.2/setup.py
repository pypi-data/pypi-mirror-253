from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="OhlcvAnalyser",
    version="0.0.2",
    packages=find_packages(),
    author="jackmappotion",
    author_email="jackmappotion@gmail.com",
    description="ohlcv analyser",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
