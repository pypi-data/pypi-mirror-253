import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Sirisha-102103715",
    version="1.0.0",
    description="TOPSIS implementation by Sirisha Singla",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sirishasingla/Topsis",
    author="Sirisha Singla",
    author_email="sirishasingla1729@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    #packages=["Topsis"],
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis.__main__:main",
        ],
    },
)