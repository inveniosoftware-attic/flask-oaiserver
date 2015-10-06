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
from config import CFG_ADMIN_EMAIL, CFG_SITE_NAME

ALLOWED_VERBS = {'Identify':identify,
                 'ListSets':list_sets,
                 'ListMetadataFormats':list_metadata_formats,
                 'ListRecords':list_records,
                 'ListIdentifiers':list_identifiers,
                 'GetRecord':get_record}

blueprint = Blueprint(
    'oaisettings',
    __name__,
    url_prefix='/oaisettings',
    static_folder="../static",
    template_folder="../templates/oaiserver/settings",
)

@blueprint.route('/')
def index():
    return render_template('index.html')
