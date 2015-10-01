from errors import BadArgumentError
from flask import request

def _get_all_request_args():
    tmp_args_dict = {}
    for key, value in request.args.iteritems:
        tmp_args_dict[key] = value
    return tmp_args_dict

def _check_args(incoming, required, optional, exlusive):
    ## TODO: include checking for duplicated arguments
    def _pop_arg_from_incoming(arg):
        try:
            return incoming.pop(arg)
        except KeyError:
            pass
        except:
            raise

    if required not in incoming:
        raise BadArgumentError("You are missing required arguments")
    if exlusive in incoming:
        for arg in exlusive:
            _pop_arg_from_incoming(arg)
        _pop_arg_from_incoming("verb")
        if len(incoming):
            raise BadArgumentError("You have passed to manu arguments together with EXLUSIVE argument.")


def _identify():
    required_arg = []
    optional_arg = []
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "This is idenification of an OAI-PMH"

def _list_sets():
    required_arg = []
    optional_arg = []
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "Here you can see all the sets"

def _list_metadata_formats():
    required_arg = []
    optional_arg = ["identifier"]
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "I am showing metadata formats here"

def _list_records():
    required_arg = ["metadataPrefix"]
    optional_arg = ["from", "until", "set"]
    exclusiv_arg = ["resumptionToken"]
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "I am going to return records from {0} until {1} in a set {2} in {3} and this is continuation of {4}".format(incoming["from"], incoming["until"], incoming["set"], incoming["metadtaPrefix"], incoming["resumptionToken"])

def _list_identifiers():
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

def _get_record():
    required_arg = ["identifier","metadataPrefix"]
    optional_arg = []
    exclusiv_arg = []
    incoming = _get_all_request_args()
    _check_args(incoming, required_arg, optional_arg, exclusiv_arg)
    return "This is the requested record with {0} identifier in format {1}".format(incoming["identifier"], incoming["metadatePrefix"])
