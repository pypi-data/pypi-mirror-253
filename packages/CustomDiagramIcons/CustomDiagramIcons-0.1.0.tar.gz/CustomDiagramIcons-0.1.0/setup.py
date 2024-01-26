from setuptools import setup, find_packages

setup(
    name="CustomDiagramIcons",
    version="0.1.0",
    author="Joshua Duma",
    author_email="joshua.duma@trader.ca",
    description="This is intended to be used in a project that uses the diagrams (diagrams as code) python package as an extention of the icons.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[
        "diagrams>=0.23.4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)