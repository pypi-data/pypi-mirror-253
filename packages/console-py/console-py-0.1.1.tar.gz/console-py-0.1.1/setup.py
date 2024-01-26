from setuptools import setup, find_packages

VERSION = "0.1.1"

setup(
    name="console-py",
    version=VERSION,
    description="A utility for printing colored messages to the console.",
    long_description=open("README.md").read(),  # Make sure to create a README.md file
    long_description_content_type="text/markdown",
    author="Sikandar Moyal",
    author_email="sikandar1838@gmail.com",
    url="https://github.com/sikandar1838/console",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    keywords=["Console", "Colorful Output", "CLI", "Text Formatting"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
