.. ZeroBounce Python API documentation master file, created by
   sphinx-quickstart on Sat Dec  2 16:19:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ZeroBounce Python API's documentation!
=================================================

zerobounce-python-api
=====================

`ZeroBounce <https://www.zerobounce.net>`__ Python API

.. code:: python

    from zerobounce import ZeroBounceAPI

    zba = ZeroBounceAPI('yourapikey____________')
    print zba.get_credits()
    print zba.validate('username@example.com')
    print zba.validatewithip('username@example.com')

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

