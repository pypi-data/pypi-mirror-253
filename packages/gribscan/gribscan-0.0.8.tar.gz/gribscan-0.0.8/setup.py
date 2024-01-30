from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gribscan",
    version="0.0.8",
    description="create indices for GRIB files and provide an xarray interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "cfgrib>=0.9.9.0",  # previous versions create a cffi error on index
        "eccodes",
        "numcodecs>=0.10.0",
        "numpy",
    ],
    extras_require={
        "docs": [
            "sphinx",
            "myst-parser",
            "sphinx-diagrams",
            "sphinx-book-theme",
        ],
    },
    entry_points={
        "console_scripts": [
            "gribscan-index=gribscan.tools:create_index",
            "gribscan-build=gribscan.tools:build_dataset",
        ],
        "numcodecs.codecs": [
            "rawgrib=gribscan.rawgribcodec:RawGribCodec",
            "gribscan.rawgrib=gribscan.rawgribcodec:RawGribCodec",
            "aec=gribscan.aeccodec:AECCodec",
        ]
    },
)
