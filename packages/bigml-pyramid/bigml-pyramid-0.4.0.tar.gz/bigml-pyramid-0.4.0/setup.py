"""Setup for package pyramid
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path, getcwd
from subprocess import check_output

from pyramid import __version__


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="bigml-pyramid",
    version=__version__,
    author="BigML Team",
    author_email="team@bigml.com",
    url="http://bigml.com/",
    description="BigML wrapper for TensorFlow",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests", "tests.*"]),
    tests_require=[
        "pynose",
    ],
    install_requires=[
        "numpy>=1.26.3,<1.27",
        "scipy>=1.12.0,<1.13.0",
        "tensorflow>=2.15,<2.16",
        "scikit-learn>=1.4.0,<1.4.1",
        "pillow>=10.2.0,<10.2.1",
        "inputimeout>=1.0.4,<1.1",
        "bigml-sensenet>=0.7.2,<0.7.3",
        "shapsplain>=0.3.0,<0.3.1",
    ],
    entry_points={
        "console_scripts": [
            "pyramid = pyramid.pyramid:main",
            "pyramid_dummy = pyramid.dummy:main",
            "pyramid_evaluate = pyramid.evaluator:main",
            "pyramid_generate = pyramid.generator:main",
            "pyramid_gpu_check = pyramid.gpu_check:main",
            "pyramid_train = pyramid.trainer:main",
        ]
    },
)
