from flask import request, render_template, g

def _get_all_request_args():
    tmp_args_dict = {}
    for key, value in request.args.iteritems():
        tmp_args_dict[key] = value
    return tmp_args_dict

def _check_args(incoming, required, optional, exlusive):
    ## TODO: include checking for duplicated arguments
    ## TODO: check for more arguments passed
    def _pop_arg_from_incoming(arg):
        try:
            return incoming.pop(arg)
        except KeyError:
            pass
        except:
            raise

    g.verb = incoming["verb"]
    g.error = {}
    _pop_arg_from_incoming("verb")
    if not set(required).issubset(set(incoming.keys())):
        missing_arguments = set(required)-set(incoming.keys())
        g.error["type"] = "badArgument"
        g.error["message"] = "You are missing required arguments: {0}".format(missing_arguments)
    if set(exlusive).issubset(set(incoming.keys())):
        for arg in exlusive:
            _pop_arg_from_incoming(arg)
        if len(incoming):
            g.error["type"] = "badArgument"
            g.error["message"] = "You have passed too many arguments together with EXLUSIVE argument."

def identify():
    required_arg = []
    optional_arg = []
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if g.error:
        return render_template("error.xml", incoming=incoming)
    else:
        return render_template("identify.xml")

def list_sets():
    required_arg = []
    optional_arg = []
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if g.error:
        return render_template("error.xml", incoming=incoming)
    else:
        return render_template("list_sets.xml",
                               incoming=incoming,
                               sets=[{'spec':'music',
                                      'name':'Music collection',
                                      'description':'This is a collection of wide range of music.'},
                                     {'spec':'music:(chopin)',
                                      'name':'Chopin collection',
                                      'description':'Collection of music composed by Chopin'},
                                     {'spec':'music:(techno)',
                                      'name':'Techno music collection'},
                                     {'spec':'pictures',
                                      'name':'Pictures collection'}
                                     ])

def list_metadata_formats():
    required_arg = []
    optional_arg = ["identifier"]
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if g.error:
        return render_template("error.xml", incoming=incoming)
    else:
        return render_template("list_metadata_formats.xml",
                               incoming=incoming,
                               formats=[{'prefix':'oai_dc',
                                         'schema':'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
                                         'namespace':'http://www.openarchives.org/OAI/2.0/oai_dc/'},
                                        {'prefix':'marcxml',
                                         'schema':'http://purl.org/dc/elements/1.1/',
                                         'namespace':'http://www.openarchives.org/OAI/1.1/dc.xsd'}
                                        ])

def list_records():
    required_arg = ["metadataPrefix"]
    optional_arg = ["from", "until", "set"]
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if g.error:
        return render_template("error.xml", incoming=incoming)
    else:
        return render_template("list_records.xml",
                               incoming=incoming,
                               records=[{'identifier':'tmpidentifier1',
                                         'datestamp':'2015-10-06',
                                         'sets':['set1']},
                                        {'identifier':'tmpidentifier2',
                                         'datestamp':'2003-04-01',
                                         'sets':['set1','set2']},
                                        {'identifier':'tmpidentifier3',
                                         'datestamp':'2014-07-13',
                                         'sets':['set3','set1']}
                                        ])

def list_identifiers():
    required_arg = ["metadataPrefix"]
    optional_arg = ["from", "until", "set"]
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if g.error:
        return render_template("error.xml", incoming=incoming)
    else:
        return render_template("list_identifiers.xml",
                               incoming=incoming,
                               records=[{'identifier':'tmpidentifier1',
                                         'datestamp':'2015-10-06',
                                         'sets':['set1']},
                                        {'identifier':'tmpidentifier2',
                                         'datestamp':'2003-04-01',
                                         'sets':['set1','set2']},
                                        {'identifier':'tmpidentifier3',
                                         'datestamp':'2014-07-13',
                                         'sets':['set3','set1']}
                                        ])

def get_record():
    required_arg = ["identifier","metadataPrefix"]
    optional_arg = []
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if g.error:
        return render_template("error.xml", incoming=incoming)
    else:
        return "This is the requested record with {0} identifier in format {1}".format(incoming["identifier"], incoming["metadatePrefix"])
