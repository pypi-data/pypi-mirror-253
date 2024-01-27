from setuptools import setup, find_packages
from combocmd.version import __version__

setup(
    name='combocmd',
    version=__version__,
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'combocmd=combocmd.combocmd:main',
        ],
    },
    python_requires='>=3.6',
)
