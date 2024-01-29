from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Control Screen Brightness via fingertips.'
LONG_DESCRIPTION = 'A package that allows to control the screen brightness using the fingertips.'

# Setting up
setup(
    name="bright-tool",
    version=VERSION,
    author="Arnab Kumar Roy",
    author_email="<arnabroy770@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'numpy', 'mediapipe', 'screen-brightness-control'],
    keywords=['python', 'video', 'brightness', 'controlling'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)