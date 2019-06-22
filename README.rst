========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |codecov|
    * - package
      - | |version| |wheel|
        | |supported-versions|
.. |docs| image:: https://readthedocs.org/projects/pywordapi/badge/?style=flat
    :target: https://readthedocs.org/projects/pywordapi
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/clchangnet/pywordapi.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/clchangnet/pywordapi

.. |codecov| image:: https://codecov.io/github/clchangnet/pywordapi/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/clchangnet/pywordapi

.. |version| image:: https://img.shields.io/pypi/v/pywordapi.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pywordapi

.. |wheel| image:: https://img.shields.io/pypi/wheel/pywordapi.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pywordapi

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pywordapi.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pywordapi

.. end-badges

Python Wordpress Api Library

* Free software: MIT license

Installation
============

::

    pip install pywordapi

Documentation
=============


https://pywordapi.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
