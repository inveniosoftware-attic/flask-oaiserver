.. _quickstart:

Quickstart
==========

This guide assumes you have successfully installed Flask-OAIServer and a working
understanding of Flask. If not, follow the installation steps and read about
Flask at http://flask.pocoo.org/docs/.


A Minimal Example
-----------------

A minimal Flask-OAIServer usage example looks like this. First create the
application and initialize the extension:

>>> from flask import Flask
>>> from flask_oaiserver import OAIServer
>>> app = Flask('myapp')
>>> ext = OAIServer(app=app)

Some Extended Example
---------------------
Flask-OAIServer also has support for ...

.. literalinclude:: ../tests/helpers.py
