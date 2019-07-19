========
Overview
========

.. start-badges

.. image:: https://readthedocs.org/projects/pywordapi/badge/?style=flat
    :target: https://readthedocs.org/projects/pywordapi
    :alt: Documentation Status

.. image:: https://travis-ci.org/clchangnet/pywordapi.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/clchangnet/pywordapi

.. image:: https://img.shields.io/pypi/v/pywordapi.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pywordapi

.. image:: https://img.shields.io/pypi/wheel/pywordapi.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pywordapi

.. image:: https://img.shields.io/pypi/pyversions/pywordapi.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pywordapi

.. end-badges

Python Wordpress Api Library

 **Pywordapi** allows a simple way to get data in and out of WordPress over HTTP, using python and Wordpress REST API.

Installation
============

To install the Pywordapi package::

    pip install pywordapi

Usage
=====

Get posts

.. code-block:: python

  from pywordapi import Pywordapi
  api_url = "https://demo.wp-api.org/"
  api = Pywordapi.WpRest(api_url)
  results = api.get_posts()

Get categories

.. code-block:: python

  from pywordapi import Pywordapi
  api_url = "https://demo.wp-api.org/"
  api = Pywordapi.WpRest(api_url)
  results = api.get_categories()

Variable **results** will return instance of type dict

Using proxy

.. code-block:: python

  from pywordapi import Pywordapi
  api_url = "https://demo.wp-api.org/"
  proxy_url = "http://username:password@IP_ADDRESS:PORT"
  api = Pywordapi.WpRest(api_url, proxy_url)
  results = api.get_posts()


Documentation
=============


https://pywordapi.readthedocs.io/
