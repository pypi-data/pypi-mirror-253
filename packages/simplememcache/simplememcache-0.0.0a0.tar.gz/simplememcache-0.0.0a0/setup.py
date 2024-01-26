import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import simplememcache module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "simplememcache"))
from simplememcache.version import VERSION  # noqa


# TODO: update long description in README.md
with open(file="README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

install_requires = []

# TODO: add test packages
tests_require = []


setup(
    name="simplememcache",
    packages=["simplememcache"],
    version=VERSION,
    url="https://github.com/aj-jaiswal007/SimpleMemCache",
    author="Amar Jaiswal",
    author_email="aj.jaiswal007@gmail.com",
    maintainer="aj-jaiswal007",
    license="MIT License",
    description="Simple mem cache client for python",
    keywords=["MEMCACHE", "CACHE", "PYTHON CACHE", "SIMPLE CACHE", "LRU CACHE"],
    install_requires=install_requires,
    extras_require={"test": tests_require},
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
