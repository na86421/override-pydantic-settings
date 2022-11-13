import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="override-pydantic-settings",  # Replace with your own username
    version="1.0.0",
    author="Junki Yoon",
    author_email="na66421@gmai.com",
    description="Override pydantic settings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/na86421/override-pydantic-settings",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
