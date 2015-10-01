# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAIServer
# Copyright (C) 2015 CERN.
#
# Flask-OAIServer is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""OAI-PMH 2.0 server."""

from __future__ import absolute_import
from flask import Blueprint, request
from invenio.base.decorators import wash_arguments
from errors import BadVerbError
from verbs import *
import sys

ALLOWED_VERBS = {'Identify':_identify,
                 'ListSets':_list_sets,
                 'ListMetadataFormats':_list_metadata_formats,
                 'ListRecords':_list_records,
                 'ListIdentifiers':_list_identifiers,
                 'GetRecord':_get_record}

blueprint = Blueprint(
    'oai2d',
    __name__,
    url_prefix='/oai',
    static_folder="../static",
    template_folder="../templates",
)

@blueprint.route('/', methods=['GET', 'POST'])
#@wash_arguments({'verb': (unicode, None)})
def server():
    verb = request.args.get("verb")
    try:
        a = ALLOWED_VERBS[verb]
        return a()
    except KeyError:
        raise BadVerbError("This is not a valid OAI-PMH verb: {0}".format(verb))
    except:
        raise
