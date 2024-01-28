import setuptools as setuptools
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='nepali-to-roman',
    version='1.0.0',  # Required
    description='A PyPi package to convert Nepali words to Romanized English Literals. Here we perform translieration and convert Devanagari words into Roman Literals. Nepali to Roman',
    url='https://github.com/Diwas524/Nepali-to-Roman-Transliteration',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Diwas Pandey, Ishparsh Uprety',
    author_email='diwaspandey524@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,

    keywords=['Nepali to roman','Nepali Transliteration', 'devanagari to English', 'devanagari', 'Diwas Pandey', 'Nepali to roman','Nepali words to roman','roman from nepali','convert nepali to roman','romanize nepali words','how to convert nepali to roman','convert Nepali to Roman'],

)
