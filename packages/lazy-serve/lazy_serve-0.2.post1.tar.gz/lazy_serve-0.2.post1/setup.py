from setuptools import find_packages, setup

setup(
    name="lazy_serve",
    version="0.2post1",
    description="A simple package for effortlessly starting HTTP servers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/lazy_serve",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
)
