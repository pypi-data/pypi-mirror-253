from setuptools import setup, find_packages

setup(
    name="Topsis-Devansh-102103620",
    version='0.0.1',
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    entry_points={'console_scripts': ['topsis = topsis.topsis:main',],},
    classifiers=['Programming Language :: Python :: 3',],
)