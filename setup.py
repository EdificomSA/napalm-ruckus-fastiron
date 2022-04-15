"""setup.py file."""
from setuptools import find_packages, setup

__author__ = 'Dominique Robert <drobert@free.fr>'
from napalm_ruckus_fastiron.version import __version__

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines()]

setup(
    name="napalm-ruckus-fastiron",
    # la version du code
    version=__version__,

    author="Dominique Robert",

    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que ça implique.
    author_email="drobert@free.fr",

    # Une description courte
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",

    # Une description longue, sera affichée pour présenter la lib
    # Généralement on dump le README ici
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX :: Linux',
    ],
    url="https://github.com/drobert31/napalm-ruckus-fastiron",
    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="MIT",

    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
