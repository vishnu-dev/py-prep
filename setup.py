import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-prep",
    version="0.0.1",
    author="",
    author_email="",
    description="A Data Prepration package for Data Enthusiasts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishnu-dev/py-prep",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
