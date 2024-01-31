

import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="topsis-102103357",
    version="0.0.3",
    description="Comparison of models using Topsis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Khushi Mittal",
    author_email="kmittal_be21@thapar.edu",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)