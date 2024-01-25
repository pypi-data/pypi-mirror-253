#!/usr/bin/python3
#
# Copyright (c) 2017-2019 NVIDIA CORPORATION. All rights reserved.
# This file is part of webloader (see TBD).
# See the LICENSE file for licensing terms (BSD-style).
#

import sys
import setuptools


if sys.version_info < (3, 6):
    sys.exit("Python versions less than 3.6 are not supported")

scripts = []

setuptools.setup(
    name="ppwebdataset",
    version = "0.2.86",
    description="Record sequential storage for deep learning.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/JunnYu/ppwebdataset",
    author="JunnYu",
    author_email="573009727@qq.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            "widsindex=wids.wids_index:main",
        ]
    },
    keywords="object store, client, deep learning",
    packages=["ppwebdataset", "ppwids"],
    python_requires=">=3.6",
    scripts=scripts,
    install_requires="braceexpand numpy pyyaml".split(),
    license_files=["LICENSE"],
)