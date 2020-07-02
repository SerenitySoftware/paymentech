from xml.etree import ElementTree

import paymentech
from paymentech.mixins import DeclarativeClass, FieldContainer
from paymentech import service


class PaymentechResource((object, FieldContainer), metaclass=DeclarativeClass):
    def serialize(self, inject=None):
        wrapper = self.meta.wrapper

        payload = ElementTree.Element(wrapper)
        for key, value in self:
            if value is None:
                continue

            serialization_key = self.fields[key].serialization_key
            child = ElementTree.SubElement(payload, serialization_key)
            child.text = value

        if inject:
            for key, value in inject:
                child = ElementTree.SubElement(payload, key)
                child.text = value

        return str(ElementTree.tostring(payload, 'unicode'))

    def save(self):
        authentication = {
            "OrbitalConnectionUsername": paymentech.configuration.get("username"),
            "OrbitalConnectionPassword": paymentech.configuration.get("password"),
            "CustomerBin": paymentech.configuration.get("bin"),
            "CustomerMerchantId": paymentech.configuration.get("merchant")
        }
        payload = self.serialize(inject=authentication)
        response = service.request(payload)

        return response
