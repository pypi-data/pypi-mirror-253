import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="topsis-dev-102117160",
    version="1.0.2",
    description="It gives the ranking to models as per the TOPSIS score.Please view the instructions so as to run the package smoothly in your terminal.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BhavyaBhalla-27/topsis-bhavya-102103345",
    author="Dev Bansal",
    author_email="devbansal03@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)