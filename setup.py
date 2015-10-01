# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAIServer
# Copyright (C) 2015 CERN.
#
# Flask-OAIServer is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys
import re


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            from configparser import ConfigParser
        config = ConfigParser()
        config.read("pytest.ini")
        self.pytest_args = config.get("pytest", "addopts").split(" ")

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# Get the version string.  Cannot be done with import!
with open(os.path.join('flask_oaiserver', 'version.py'), 'r') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')


setup(
    name='Flask-OAIServer',
    version=version,
    url='http://github.com/inveniosoftware/flask-oaiserver/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='Flask-OAIServer allows you to quickly add an OAuth2 '
                'provider to your Flask application.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10.1',
        'six',
        'Flask-OAuthlib>=0.6.0',
        'Flask-Registry>=0.2.0',
        'Flask-Breadcrumbs>=0.1.0',
        'Flask-Menu>=0.1.0',
        "Flask-Login>=0.2.7",
        "Flask-WTF>=0.10.0",
        "WTForms>=2.0",
        "wtforms-alchemy>=0.12.6",
        "SQLAlchemy>=0.8.3",
        "SQLAlchemy-Utils",
    ],
    tests_require=[
        'pytest-cache>=1.0',
        'pytest-cov>=1.8.0',
        'pytest-pep8>=1.0.6',
        'pytest>=2.6.1',
        'coverage',
        'mock',
        'pep257',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
    ],
    cmdclass={'test': PyTest},
)
