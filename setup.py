from setuptools import setup, find_packages


__name__ = "kikite"
__version__ = "1.0.0"
__url__ = "https://github.com/HSouch/kikite"
__author__ = "Harrison Souchereau"
__author_email__ = "harrison.souchereau@yale.edu"


setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description="Chord determination from audio files.",
    url=__url__,
    packages=find_packages(),

    )
