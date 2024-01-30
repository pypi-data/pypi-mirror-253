from setuptools import setup, find_packages

setup(
    name='pst_wrinkle',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'malariagen-data'
        'igv_notebook',  
        'matplotlib',
        'cartopy',
        'geopandas',
        'numpy',
        'pandas'
    ],
)