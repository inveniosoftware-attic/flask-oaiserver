# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAIServer
# Copyright (C) 2015, 2016 CERN.
#
# Flask-OAIServer is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from flask import render_template, g


class BadArgumentError(Exception):

    """OAI-PMH bad argument error.

    The request includes illegal arguments, is missing required arguments,
    includes a repeated argument, or values for arguments have an illegal
    syntax.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a BadArgumentError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "BadArgumentError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")


class BadResumptionTokenError(Exception):

    """OAI-PMH resumption token error.

    The value of the resumptionToken argument is invalid or expired.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a BadResumptionTokenError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "BadResumptionTokenError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")


class BadVerbError(Exception):

    """Not a valid OAI-PMH verb.

    Value of the verb argument is not a legal OAI-PMH verb, the verb argument
    is missing, or the verb argument is repeated.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a BadVerbError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "BadVerbError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")

    def __repr__(self):
        """Print method representation."""
        g.error = {}
        g.error['message'] = self.message
        g.error['type'] = "badVerb"
        return render_template("error.xml")


class CannotDisseminateFormatError(Exception):

    """Not a valid OAI-PMH format.

    The metadata format identified by the value given for the metadataPrefix
    argument is not supported by the item or by the repository.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a CannotDisseminateFormatError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "CannotDisseminateFormatError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")


class IdDoesNotExistError(Exception):

    """Id does not exist.

    The value of the identifier argument is unknown or illegal in this
    repository.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a IdDoesNotExistError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "IdDoesNotExistError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")


class NoRecordsMatchError(Exception):

    """No records found.

    The combination of the values of the from, until, set and metadataPrefix
    arguments results in an empty list.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a NoRecordsMatchError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "NoRecordsMatchError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")


class NoMetadataFormatsError(Exception):

    """There are no metadata formats available for the specified item."""

    def __init__(self, message, **kwargs):
        """Instanciate a NoMetadataFormatsError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "NoMetadataFormatsError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")


class NoSetHierarchyError(Exception):

    """No OAI-PMH sets available.

    Raised when there is no sets defined.
    """

    def __init__(self, message, **kwargs):
        """Instanciate a NoSetHierarchyError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "NoSetHierarchyError({0}, \
                payload: {1}".format(repr(self.message),
                                     repr(self.payload) or "None")
