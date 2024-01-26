#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# requirements = ['Click>=7.0', ]
with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

test_requirements = [ ]

setup(
    author="Hongdeng Jian",
    author_email='jianhd@radi.ac.cn',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Cutci is a library to calculate Human Thermal Comfort Index (UTCI) by GPU-accelerated computing with CuPy.",
    entry_points={
        'console_scripts': [
            'cutci=cutci.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cutci',
    name='cutci',
    packages=find_packages(include=['cutci', 'cutci.*', 'cutci_*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jianhongdeng/cutci',
    version='1.0.1',
    zip_safe=False,
)
