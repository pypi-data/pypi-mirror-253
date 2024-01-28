from setuptools import find_packages, setup


setup(
    name="spiders",
    version="0.0.2",
    description="Internet web scraper",
    package_dir={"spiders": "./"},
    packages=find_packages(where="./"),
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
