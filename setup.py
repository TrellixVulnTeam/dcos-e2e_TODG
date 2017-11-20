"""
Setup script for DC/OS End to End tests.
"""

from setuptools import find_packages, setup

VERSION = '2017.11.15.0'

DEPENDENCY_LINKS = []

with open('requirements.txt') as requirements:
    INSTALL_REQUIRES = []
    for line in requirements.readlines():
        if line.startswith('#'):
            continue
        if line.startswith('--find-links --no-index'):
            _, link = line.split('--find-links --no-index ')
            DEPENDENCY_LINKS.append(link)
        else:
            INSTALL_REQUIRES.append(line)

with open('dev-requirements.txt') as dev_requirements:
    DEV_REQUIRES = []
    for line in dev_requirements.readlines():
        if not line.startswith('#'):
            DEV_REQUIRES.append(line)

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

TEST_UTILS_SHA = 'd983e3c1e7a65576e8828dccd7429e844560202f'

setup(
    name='DC/OS E2E',
    version=VERSION,
    author='Adam Dangoor',
    author_email='adangoor@mesosphere.com',
    description='Test helpers for testing DC/OS end to end.',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where='src'),
    zip_safe=False,
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    extras_require={
        'dev': DEV_REQUIRES,
    },
    classifiers=[
        'Operating System :: POSIX',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.5',
    ],
    dependency_links=DEPENDENCY_LINKS,
)
