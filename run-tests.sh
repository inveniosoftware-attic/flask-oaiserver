# This file is part of Flask-OAIServer
# Copyright (C) 2015 CERN.
#
# Flask-OAIServer is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

pydocstyle --ignore=D100,D101,D102,D103 flask_oaiserver
sphinx-build -qnNW docs docs/_build/html
python setup.py test
