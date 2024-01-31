from setuptools import setup, find_packages
import os

cwd = os.path.dirname(os.path.abspath(__file__))

requirements = open(os.path.join(cwd, "requirements.txt"), "r").readlines()

with open("README.md", "r", encoding="utf-8") as readme_file:
    README = readme_file.read()


setup(
    name='slovene_form_generator',
    version='0.0.17',
    author = "Peter Pisljar",
    description = "slovene word inflector / form generator",
    long_description=README,
    install_requires=requirements,
    packages=find_packages(),
    python_requires=">=3.8.0, <3.12",
    include_package_data=True,
)