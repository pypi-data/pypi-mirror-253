from setuptools import setup, find_packages

#reads the file README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='test1_H4upackage',
    version='6.6.6',
    packages=find_packages(),
    install_requires=[],
    author="Luis González",
    description="A test of project uploading (Hack4u courses)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io"

)
