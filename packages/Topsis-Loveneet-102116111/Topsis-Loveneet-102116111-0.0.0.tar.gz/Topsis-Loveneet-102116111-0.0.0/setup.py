import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Loveneet-102116111",
    version="0.0.0",
    description="TOPSIS implementation by Loveneet Kaur",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kaurneetlove/Topsis-Loveneet-102116111",
    author="Loveneet Kaur",
    author_email="kaurneetlove@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "sys",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis._main_:main",
        ],
    },
)