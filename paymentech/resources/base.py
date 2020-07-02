from xml.etree import ElementTree

from paymentech.mixins import DeclarativeClass, FieldContainer


class PaymentechResource((object, FieldContainer), metaclass=DeclarativeClass):
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
