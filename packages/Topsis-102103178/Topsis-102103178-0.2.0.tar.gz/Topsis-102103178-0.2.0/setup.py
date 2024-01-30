# setup.py
from setuptools import setup, find_packages

setup(
    name='Topsis-102103178',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
