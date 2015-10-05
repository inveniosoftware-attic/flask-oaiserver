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
from flask import (Blueprint,
                   request,
                   render_template,
                   g,
                   make_response)
from errors import BadVerbError
from views.verbs import (identify,
                         list_sets,
                         list_metadata_formats,
                         list_records,
                         list_identifiers,
                         get_record)
from datetime import datetime

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
def server():
    verb = request.args.get("verb")
    g.response_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%Sz")
    try:
        a = ALLOWED_VERBS[verb]
        output_xml = a()
        response = make_response(output_xml)
        response.headers["Content-Type"] = "application/xml"
        return response
    except KeyError:
        raise BadVerbError("This is not a valid OAI-PMH verb: {0}".format(verb))
    except:
        raise


@blueprint.route('/config')
def index():
    return render_template('oaiserver/config/index.html')
