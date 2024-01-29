""""steup.py"""
import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.2.1'
DESCRIPTION = ''
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="osrs-python-bot",
    version=VERSION,
    author="osrs-bots",
    author_email="",
    url="https://github.com/osrs-bots/osrs-python-bot",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyautogui', 'pynput'],
    keywords=['osrs-bots'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
