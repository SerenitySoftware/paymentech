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
