class BadArgumentError(Exception):
    """The request includes illegal arguments, is missing required arguments, includes a repeated argument, or values for arguments have an illegal syntax."""
    def __init__(self, message, **kwargs):
        """Instanciate a BadArgumentError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "BadArgumentError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class BadResumptionTokenError(Exception):
    """The value of the resumptionToken argument is invalid or expired."""
    def __init__(self, message, **kwargs):
        """Instanciate a BadResumptionTokenError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "BadResumptionTokenError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class BadVerbError(Exception):
    """Value of the verb argument is not a legal OAI-PMH verb, the verb argument is missing, or the verb argument is repeated."""
    def __init__(self, message, **kwargs):
        """Instanciate a BadVerbError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "BadVerbError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class CannotDisseminateFormatError(Exception):
    """The metadata format identified by the value given for the metadataPrefix argument is not supported by the item or by the repository."""
    def __init__(self, message, **kwargs):
        """Instanciate a CannotDisseminateFormatError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "CannotDisseminateFormatError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class IdDoesNotExistError(Exception):
    """The value of the identifier argument is unknown or illegal in this repository."""
    def __init__(self, message, **kwargs):
        """Instanciate a IdDoesNotExistError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "IdDoesNotExistError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class NoRecordsMatchError(Exception):
    """The combination of the values of the from, until, set and metadataPrefix arguments results in an empty list."""
    def __init__(self, message, **kwargs):
        """Instanciate a NoRecordsMatchError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "NoRecordsMatchError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class NoMetadataFormatsError(Exception):
    """There are no metadata formats available for the specified item."""
    def __init__(self, message, **kwargs):
        """Instanciate a NoMetadataFormatsError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "NoMetadataFormatsError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")


class NoSetHierarchyError(Exception):
    """Raised when there is no sets defined."""

    def __init__(self, message, **kwargs):
        """Instanciate a NoSetHierarchyError object."""
        Exception.__init__(self)
        self.message = message
        self.payload = kwargs

    def __str__(self):
        """String representation."""
        return "NoSetHierarchyError({0}, payload: {1}".format(repr(self.message), repr(self.payload) or "None")
