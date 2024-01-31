import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.8"
DESCRIPTION = "An internal package to allow for easy uploading of labels to the Ward Analytics API."
LONG_DESCRIPTION = (
    "An internal package to allow for easy uploading of labels to the Ward Analytics API."
)

setup(
    name="ward-labels-upload",
    version=VERSION,
    author="Ward Analytics",
    author_email="<gabriel.vieira@vdspar.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["pydantic", "requests", "tqdm"],
    keywords=["Internal"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
