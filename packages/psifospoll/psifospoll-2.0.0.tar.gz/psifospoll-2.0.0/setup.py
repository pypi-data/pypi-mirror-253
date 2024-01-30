from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="psifospoll",
    version="2.0.0",
    author="Fernanda Macías",
    author_email="fernanda.macias@ug.uchile.cl",
    description="PsifosPoll is a python library for different voting methods",
    packages=find_packages(),
    url="https://github.com/clcert/psifospoll",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
