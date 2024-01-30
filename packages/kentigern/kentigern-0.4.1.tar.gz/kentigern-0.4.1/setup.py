"""Sphinx Bootstrap Theme package."""
import os
from setuptools import setup, find_packages


###############################################################################
# Environment and Packages.
###############################################################################
# Don't copy Mac OS X resource forks on tar/gzip.
os.environ['COPYFILE_DISABLE'] = "true"

# Packages.
MOD_NAME = "kentigern"
PKGS = [x for x in find_packages() if x.split('.')[0] == MOD_NAME]


###############################################################################
# Helpers.
###############################################################################
def read_file(name):
    """Read file name (without extension) to string."""
    cur_path = os.path.dirname(__file__)
    exts = ('txt', 'rst')
    for ext in exts:
        path = os.path.join(cur_path, '.'.join((name, ext)))
        if os.path.exists(path):
            with open(path, 'rt') as file_obj:
                return file_obj.read()

    return ''


###############################################################################
# Setup.
###############################################################################
setup(
    name="kentigern",
    description="A modern-looking Sphinx theme",
    #long_description=read_file("README"),
    url="https://code.daniel-williams.co.uk/kentigern",
    # use_scm_version={"local_scheme": "no-local-version"},
    # setup_requires=['setuptools_scm'],
    version="0.4.1",
    author="Daniel Williams",
    author_email="mail@daniel-williams.co.uk",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],
    install_requires=[
        "setuptools",
        "sphinx",
        "sphinxcontrib-jquery"
    ],
    entry_points = {
        'sphinx.html_themes': [
            'kentigern = kentigern',
        ]
    },
    packages=PKGS,
    include_package_data=True,
)
