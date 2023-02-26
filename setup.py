#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    #"hddcoin-blockchain==3.0.0",
    #"hddcoin-blockchain@git+https://github.com/HDDcoin-Network/hddcoin-blockchain.git",
	"hddcoin-blockchain@git+https://github.com/HDDcoin-Network/hddcoin-blockchain-beta.git",

]

dev_dependencies = [
    "black==21.12b0",
    "pytest",
    "pytest-env",
]

setup(
    name="HAT_admin_tool",
    version="0.0.1",
    author="HDDcoin Network",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "cats = cats.cats:main",
            "secure_the_bag = cats.secure_the_bag:main",
            "unwind_the_bag = cats.unwind_the_bag:main"
        ],
    },
    author_email="dev@hddcoin.org",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/HDDcoin-Network",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Tools to administer issuance and redemption of a HDDcoin Asset Token or HAT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/HDDcoin-Network/HAT-admin-tool",
        "Source": "https://github.com/HDDcoin-Network/HAT-admin-tool",
    },
)
