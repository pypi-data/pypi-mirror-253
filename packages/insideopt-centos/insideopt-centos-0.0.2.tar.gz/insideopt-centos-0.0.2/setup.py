#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Meinolf Sellmann",
    author_email='info@insideopt.com',
    python_requires='>=3.6.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="InsideOpt Seeker Distribution for CentOS",
    install_requires=requirements,
    long_description=readme, 
    keywords='insideopt, seeker, optimization',
    name='insideopt-centos',
    test_suite='tests',
    version='0.0.2',
    packages=find_packages(include=['seekercentos', 'seekercentos.*', '*.so', '*.a']),
    package_data={'seekercentos': ['*.a', '*.so', 'seekercentos.py', 'bin/*', 'scripts/*']},
    zip_safe=False,
)
