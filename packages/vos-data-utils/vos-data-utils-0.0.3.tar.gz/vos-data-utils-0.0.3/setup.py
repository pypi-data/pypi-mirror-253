import setuptools
from vdutils import (
    author,
    version,
    description
)


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vos-data-utils",
    version=version,
    author=author,
    author_email="dev@valueofspace.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={"vdutils": [
        "data/*.txt", 
        "data/*.pkl", 
        "data/pnu/*.pkl"
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "symspellpy",
        "pandas",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'shortcut1 = package.module:func',
        ],
        'gui_scripts': [
            'shortcut2 = package.module:func',
        ]
    }
)
