from setuptools import find_packages, setup

setup(
    name="lazy_serve",
    version="0.2.1",
    description="A simple package for effortlessly starting multiple threaded HTTP servers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Michael Pilosov",
    author_email="mm@clfx.cc",
    url="https://git.mlden.com/mm/lazy_serve.git",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
)
