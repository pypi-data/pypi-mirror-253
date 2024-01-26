from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='vanilla-knn',
    version='0.1.1',
    packages=['vanilla_knn'],
    author='RayVil',
    description='Uma implementação simples do algoritmo KNN em Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RayVilaca/vanilla-knn',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)