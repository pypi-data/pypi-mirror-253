from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="tailwind-palette",
    version="1.0.1",
    description="A Python package for working with the Tailwind CSS color palette.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Noah Youngs",
    packages=find_packages(),
)
