from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

VERSION = '1.0'
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
    entry_points={
        'console_scripts': [
            'bright-tool = bright_tool:run_bright_tool'
        ]
    },
    install_requires=['opencv-python', 'numpy', 'mediapipe', 'screen-brightness-control'],
    keywords=['python', 'video', 'brightness', 'controlling'],
)