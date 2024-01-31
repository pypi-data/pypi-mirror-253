import os
import pathlib
import re
import subprocess

from setuptools import setup
import setuptools
from jejudo._version import __version__

STABLE_STAGE = True

ROOT = pathlib.Path(__file__).parent

EXTRA_REQUIRES = {}


for feature in (ROOT / "requirements").glob("*.txt"):
    with open(feature, "r", encoding="utf-8") as f:
        EXTRA_REQUIRES[feature.with_suffix("").name] = f.read().splitlines()
REQUIREMENTS = EXTRA_REQUIRES.pop("_")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jejudo", ## 소문자 영단어
    version=__version__, ##
    license="MIT",
    author="blket.dev", ## ex) Sunkyeong Lee
    author_email=None, ##
    description="discord is py-cord bot debug tools\nA py-cord extension including useful tools for bot development and debugging.", ##
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=None, ##
    packages=["jejudo","jejudo.core","jejudo.repl","jejudo.core.shim","jejudo.core.work"],

    keywords="jejudo, jishkucord, py-cord, discord, cog, repl, extension, jishaku",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    python_requires='>=3.9',
)