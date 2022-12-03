from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="1.0",
    author="Reemoh",
    author_email="geeta.reemoh@fau.de",
    packages=find_packages(),
    install_requires=["numpy","turtles"],
)