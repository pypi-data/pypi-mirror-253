from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='geoproximity',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[],
    author='Niraj Adhikari',
    author_email='nrjadkry@gmail.com',
    description='A Python package for geospatial distance calculations and proximity-related functions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nrjadkry/geoproximity',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: GIS',
        'Programming Language :: Python :: 3.8',
    ],
)
