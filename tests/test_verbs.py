# -*- coding: utf-8 -*-
#
# This file is part of Flask-OAIServer
# Copyright (C) 2015 CERN.
#
# Flask-OAIServer is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

from __future__ import absolute_import
from unittest import TestCase
from flask import g
from flask_oaiserver.oai import app
from flask_oaiserver.config import *
import re


class FlaskTestCase(TestCase):

    """Mix-in class for creating the Flask application"""

    def setUp(self):
        self.app = app
        self.app.testing = True
        pass

    def tearDown(self):
        pass


class TestVerbs(FlaskTestCase):

    """Tests OAI-PMH verbs"""

    def test_no_verb(self):
        with self.app.test_client() as c:
            result = c.get('/oai2d', follow_redirects=True)
            response_date = getattr(g, 'response_date', None)
            expected = """<?xmlversion="1.0"encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/
         http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>{0}</responseDate>
    <error code="badValue">This is not a valid OAI-PMH verb:None</error>
</OAI-PMH>""".format(response_date)
            result_data = result.data.decode("utf-8")
            result_data = re.sub(' +', '', result_data.replace('\n', ''))
            expected = re.sub(' +', '', expected.replace('\n', ''))
            self.assertEqual(result_data, expected)

    def test_wrong_verb(self):
        with self.app.test_client() as c:
            result = c.get('/oai2d?verb=Aaa', follow_redirects=True)
            response_date = getattr(g, 'response_date', None)
            expected = """<?xmlversion="1.0"encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/
         http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>{0}</responseDate>
    <error code="badValue">This is not a valid OAI-PMH verb:Aaa</error>
</OAI-PMH>""".format(response_date)
            result_data = result.data.decode("utf-8")
            result_data = re.sub(' +', '', result_data.replace('\n', ''))
            expected = re.sub(' +', '', expected.replace('\n', ''))
            self.assertEqual(result_data, expected)

    def test_identify(self):
        ########
        # TODO - remove all placeholder values
        ########
        with self.app.test_client() as c:
            result = c.get('/oai2d?verb=Identify', follow_redirects=True)
            response_date = getattr(g, 'response_date', None)
            expected = """<?xml version="1.0" encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/
         http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>{0}</responseDate>
    <request verb="Identify">http://memory.loc.gov/cgi-bin/oai</request>
    <Identify>
        <repositoryName>{1}</repositoryName>
        <baseURL>http://memory.loc.gov/cgi-bin/oai</baseURL>
        <protocolVersion>2.0</protocolVersion>
        <adminEmail>{2}</adminEmail>
        <earliestDatestamp>1990-02-01T12:00:00Z</earliestDatestamp>
        <deletedRecord>transient</deletedRecord>
        <granularity>YYYY-MM-DDThh:mm:ssZ</granularity>
        <compression>deflate</compression>
     </Identify>
</OAI-PMH>""".format(response_date, CFG_SITE_NAME, CFG_ADMIN_EMAIL)
            result_data = result.data.decode("utf-8")
            result_data = re.sub(' +', '', result_data.replace('\n', ''))
            expected = re.sub(' +', '', expected.replace('\n', ''))
            self.assertEqual(result_data, expected)

    def test_identify_with_additional_args(self):
        with self.app.test_client() as c:
            result = c.get('/oai2d?verb=Identify&notAValidArg=True',
                           follow_redirects=True)
            response_date = getattr(g, 'response_date', None)
            expected = """<?xmlversion="1.0"encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/
         http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>{0}</responseDate>
    <request verb="Identify" notAValidArg="True">
        http://an.oa.org/OAI-script
    </request>
    <error code="badArgument">
        You have passed too many arguments together withEXLUSIVE argument.
    </error>
</OAI-PMH>""".format(response_date)
            result_data = result.data.decode("utf-8")
            result_data = re.sub(' +', '', result_data.replace('\n', ''))
            expected = re.sub(' +', '', expected.replace('\n', ''))
            self.assertEqual(result_data, expected)
