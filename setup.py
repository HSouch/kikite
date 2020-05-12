from setuptools import setup, find_packages


__name__ = "kikite"
__version__ = "1.0.2"
__url__ = "https://github.com/HSouch/kikite"
__author__ = "Harrison Souchereau"
__author_email__ = "harrison.souchereau@yale.edu"


req_file = open('required_packages.txt')
__install_requires__ = [x.strip("\n") for x in req_file.readlines()]


setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description="Chord determination from audio files.",
    long_description_content_type="text/markdown",
    url=__url__,
    packages=find_packages(),

    install_requires=__install_requires__,
    include_package_data=True
    )
