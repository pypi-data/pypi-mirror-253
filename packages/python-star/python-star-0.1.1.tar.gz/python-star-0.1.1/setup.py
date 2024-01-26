from setuptools import setup
from src.star.version import __version__


setup(
    name="python-star",
    version=__version__,
    license="MIT",
    description="A command-line tool for simplifying project setup and development tasks.",
    long_description=open("README.md").read(),  # Make sure to create a README.md file
    long_description_content_type="text/markdown",
    author="Sikandar Moyal",
    author_email="sikandar1838@gmail.com",
    url="https://github.com/sikandar1838/star",
    packages=["star"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "star=star.__main__:CLI",
        ],
    },
    keywords=[
        "CLI",
        "project setup",
        "testing",
        "development",
        "automation",
        "scripting",
        "workflow",
        "convenience",
        "productivity",
        "deployment",
        "utility",
        "developer tool",
        "single command",
    ],
    install_requires=[
        "console-py==0.1.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
