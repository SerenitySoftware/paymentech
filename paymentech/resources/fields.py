class DataField(object):

    def __init__(self, serialization_key, default=None, max_length=None):
        self.serialization_key = serialization_key
        self.default = default
        self.max_length = max_length
