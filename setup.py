
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gui-dice-roller',

    version='0.2.2',

    description='GUI for D&D like dice roller',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/MARS-XI/Dice-Roller',

    author='Marcello Lamonaca',

    author_email='',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Role-Playing',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
        'Natural Language :: English'
    ],

    keywords='D&D dice-roller python GUI',

    packages=find_packages(),

    python_requires='>=3.7',

    install_requires=['tkinter'],
)
