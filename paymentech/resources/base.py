import six
from xml.etree import ElementTree

from paymentech.mixins import DeclarativeClass


class PaymentechResource(object, metaclass=DeclarativeClass):

    def __init__(self, *args, **kwargs):
        self.data = {}
        for key, value in six.iteritems(kwargs):
            if key in self.fields:
                setattr(self, key, kwargs[key])

    def __iter__(self):
        print("Iterate")
        # Only iterate through the declarative fields, since we inherit dict
        for key, field in six.iteritems(self.fields):
            yield key, self.data.get(key, field.default)

    def __setattr__(self, key, value):
        # Only set an attribute if it's part of the declarative fields
        if key == "data":
            super().__setattr__(key, value)
        elif key in self.fields:
            self.data[key] = value

    def __getattr__(self, key):
        # Return the value that we stored on the data property during
        # __setattr__ for attribute access
        if key in self.fields:
            return self.data.get(key, None)

        return None

    def __getitem__(self, key, encode=True):
        # Return the encoded value that we stored during __setattr__ for
        # dict-like access (i.e. for JSON encoding)
        if key in self.fields:
            value = super().__getitem__(key)
            return value

        return None

    def serialize(self):
        wrapper = self.meta.wrapper

        payload = ElementTree.Element(wrapper)
        for key, value in self:
            if value is None:
                continue

            serialization_key = self.fields[key].serialization_key
            child = ElementTree.SubElement(payload, serialization_key)
            child.text = value

        return str(ElementTree.tostring(payload, 'unicode'))
