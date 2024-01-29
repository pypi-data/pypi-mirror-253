import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    # setup_requires=['wheel'],
    name="Topsis-Kushagre-102103612",
    version="1.0.0",
    description="Topsis",
    
    url="https://github.com/Kushagrekaushik/Topsis-Implementation",
    author="Kushagre Kaushik",
    author_email="Kushagrekaushik2003@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["Topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "perform_topsis=perform_topsis.__main__:main",
        ]
    },
)