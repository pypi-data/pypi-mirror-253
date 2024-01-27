from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="vihub",
    version="0.0.4",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "vihub = vihub:hello",
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
