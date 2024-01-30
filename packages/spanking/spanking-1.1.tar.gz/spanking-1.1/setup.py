from setuptools import setup, find_packages

with open("README.md", "r") as f:
  description = f.read()

setup(
  name="spanking",
  author="Rishiraj Acharya",
  author_email="heyrishiraj@gmail.com",
  url="https://github.com/rishiraj/spanking",
  license="Apache 2.0",
  version="1.1",
  packages=find_packages(),
  install_requires=[],
  entry_points={
    "console_scripts": [
      "spanking-booty = spanking:booty",
    ],
  },
  long_description=description,
  long_description_content_type="text/markdown",
)