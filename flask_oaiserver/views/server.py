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
from flask import Blueprint, request, render_template
from invenio.base.decorators import wash_arguments
from errors import BadVerbError
from views.verbs import (identify,
                         list_sets,
                         list_metadata_formats,
                         list_records,
                         list_identifiers,
                         get_record)
import sys

ALLOWED_VERBS = {'Identify':identify,
                 'ListSets':list_sets,
                 'ListMetadataFormats':list_metadata_formats,
                 'ListRecords':list_records,
                 'ListIdentifiers':list_identifiers,
                 'GetRecord':get_record}

blueprint = Blueprint(
    'oai2d',
    __name__,
    url_prefix='/oai2d',
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


@blueprint.route('/config')
def index():
    return render_template('oaiserver/index.html')
