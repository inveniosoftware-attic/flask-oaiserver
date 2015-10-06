from errors import BadArgumentError
from flask import request, render_template

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

    _pop_arg_from_incoming("verb")
    if not set(required).issubset(set(incoming.keys())):
        raise BadArgumentError("You are missing required arguments")
    if set(exlusive).issubset(set(incoming.keys())):
        for arg in exlusive:
            _pop_arg_from_incoming(arg)
        if len(incoming):
            raise BadArgumentError("You have passed too many arguments together with EXLUSIVE argument.")


def identify():
    required_arg = []
    optional_arg = []
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return render_template("oaiserver/xml/identify.xml")

def list_sets():
    required_arg = []
    optional_arg = []
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "Here you can see all the sets"

def list_metadata_formats():
    required_arg = []
    optional_arg = ["identifier"]
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "I am showing metadata formats here"

def list_records():
    required_arg = ["metadataPrefix"]
    optional_arg = ["from", "until", "set"]
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "I am going to return records from {0} until {1} in a set {2} in {3} and this is continuation of {4}".format(incoming["from"], incoming["until"], incoming["set"], incoming["metadtaPrefix"], incoming["resumptionToken"])

def list_identifiers():
    required_arg = ["metadataPrefix"]
    optional_arg = ["from", "until", "set"]
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    if "from" not in incoming:
        incoming["from"] = None
    if "until" not in incoming:
        incoming["from"] = None
    if "set" not in incoming:
        incoming["from"] = None
    if "metadataPrefix" not in incoming:
        incoming["metadataPrefix"] = None
    return "I am going to return identifiers from {0} until {1} in a set {2} in {3} and this is continuation of {4}".format(incoming["from"], incoming["until"], incoming["set"], incoming["metadtaPrefix"], incoming["resumptionToken"])

def get_record():
    required_arg = ["identifier","metadataPrefix"]
    optional_arg = []
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "This is the requested record with {0} identifier in format {1}".format(incoming["identifier"], incoming["metadatePrefix"])
