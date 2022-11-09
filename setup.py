import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="md_ext",
    version="0.0.3",
    author="Omid Raha",
    author_email="or@omidraha.com",
    description="Markdown extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omidraha/md_ext",
    download_url="https://github.com/omidraha/md_ext/archive/refs/tags/0.0.3.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pytest==7.1.2'],
)

