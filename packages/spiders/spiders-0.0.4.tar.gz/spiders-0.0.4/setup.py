from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="spiders",
    version="0.0.4",
    description="Internet web scraper",
    long_description=long_description,
    packages=find_packages(),
    url="https://github.com/saurabhmahra91/spiderstore.git",
    author="Saurabh Kumar Mahra",
    author_email="sourabhmahra91@gmail.com",
    license_files=("LICENSE.txt"),
    install_requires=[],
    extras_requires={
        "dev": ["twine>=4.0.2"]
    },
    python_requires=">=3.11",
)
