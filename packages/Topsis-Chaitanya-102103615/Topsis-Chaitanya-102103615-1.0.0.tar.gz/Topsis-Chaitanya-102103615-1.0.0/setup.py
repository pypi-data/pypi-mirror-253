import pathlib
from setuptools import setup

# The directory containing this file


# The text of the README file


# This call to setup() does all the work
setup(
    setup_requires=['wheel'],
    name="Topsis-Chaitanya-102103615",
    version="1.0.0",
    description="Topsis",
    # long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/CHAITANYA2605/Topsis_implementation",
    author="Chaitanya Arora",
    author_email="chaitanyaarora26@gmail.com",
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