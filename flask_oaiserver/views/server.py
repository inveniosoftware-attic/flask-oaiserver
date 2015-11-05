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
from ..views.verbs import (identify,
                           list_sets,
                           list_metadata_formats,
                           list_records,
                           list_identifiers,
                           get_record)
from datetime import datetime
from ..config import CFG_ADMIN_EMAIL, CFG_SITE_NAME

ALLOWED_VERBS = {'Identify': identify,
                 'ListSets': list_sets,
                 'ListMetadataFormats': list_metadata_formats,
                 'ListRecords': list_records,
                 'ListIdentifiers': list_identifiers,
                 'GetRecord': get_record}

blueprint = Blueprint(
    'oai2d',
    __name__,
    url_prefix='/oai2d',
    static_folder="../static",
    template_folder="../templates/oaiserver/server"
)


@blueprint.route('/', methods=['GET', 'POST'])
def server():
    verb = request.args.get("verb")
    g.response_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%Sz")
    g.admin_email = CFG_ADMIN_EMAIL
    g.repository_name = CFG_SITE_NAME
    try:
        a = ALLOWED_VERBS[verb]
    except KeyError:
        g.error = {}
        g.error['message'] = "This is not a valid OAI-PMH verb: \
                              {0}".format(verb)
        g.error['type'] = "badValue"
        return render_template("error.xml")

    output_xml = a()
    response = make_response(output_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
