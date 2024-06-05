"""setup.py file."""
from setuptools import find_packages, setup

__author__ = 'Edificom SA <dev-auto@edificom.ch>'
from napalm_ruckus_fastiron.version import __version__

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines()]

setup(
    name="napalm-ruckus-fastiron",
    version=__version__,

    author="Edificom SA",
    author_email="dev-auto@edificom.ch",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",

    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
    ],
    url="https://github.com/EdificomSA/napalm-ruckus-fastiron",
    license="MIT",

    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
