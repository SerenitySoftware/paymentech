import six


from paymentech.resources.fields import DataField


class DeclarativeClass(type):
    """Metaclass definition that handles creating a hidden property to store a
    dict of the fields"""

    def __new__(cls, name, bases, attrs):
        # Loop through all the requested attributes, but filter out the
        # DeclarativeFields so that we can store them separately. Removing them
        # from the generator.attrs allows __getattr__ to work in the
        # DeclarativeBase, since it requires the attribute to actually be
        # missing to run.
        filtered_attrs = {}
        fields = {}
        meta = None
        for name, attr in attrs.items():
            if isinstance(attr, DataField):
                fields[name] = attr
            elif name == "Meta":
                meta = attr
            else:
                filtered_attrs[name] = attr

        new = super().__new__(cls, name, bases, filtered_attrs)
        new.meta = meta
        new.fields = fields

        return new


class FieldContainer:
    def __init__(self, *args, **kwargs):
        self.data = {}
        for key, value in six.iteritems(kwargs):
            if key in self.fields:
                setattr(self, key, kwargs[key])

    def __iter__(self):
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
