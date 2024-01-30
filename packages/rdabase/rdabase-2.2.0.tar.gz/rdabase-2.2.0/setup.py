from setuptools import setup, find_packages

setup(
    name="rdabase",
    version="2.2.0",
    description="Redistricting analytics data",
    url="https://github.com/rdatools/rdabase",
    author="alecramsay",
    author_email="a73cram5ay@gmail.com",
    license="MIT",
    packages=[
        "rdabase",
    ],
    install_requires=[
        "fiona",
        "geopandas",
        "libpysal",
        "shapely",
    ],
    zip_safe=False,
)
