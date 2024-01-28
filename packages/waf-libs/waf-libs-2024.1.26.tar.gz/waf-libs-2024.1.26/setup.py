"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import pathlib

from codecs import open
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

with open((here / "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="waflibs",
    version=open((here / "VERSION")).read().strip(),
    description="waf libs",
    long_description=long_description,
    url="https://bitbucket.org/waf/waf-libs",
    author="Felix Wong",
    author_email="felix@waf.hk",
    license="Apache",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="waflibs waf libs waf-libs lib waflib",
    packages=find_packages("source"),
    package_dir={"": "source"},
    install_requires=(here / 'requirements.txt').read_text(encoding='utf-8').splitlines(),
    extras_require={
        "test": ["unittest", "nose"],
    },
    test_suite="nose2.collector.collector",
)
