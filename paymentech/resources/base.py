from xml.etree import ElementTree

import paymentech
from paymentech.mixins import DeclarativeClass, FieldContainer
from paymentech import service


class PaymentechResource(FieldContainer, metaclass=DeclarativeClass):
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
            for key, value in inject.items():
                child = ElementTree.SubElement(payload, key)
                child.text = value

        return str(ElementTree.tostring(payload, 'unicode'))

    def transact(self):
        authentication = {
            "OrbitalConnectionUsername": paymentech.configuration.get("username"),
            "OrbitalConnectionPassword": paymentech.configuration.get("password"),
            "BIN": paymentech.configuration.get("bin"),
            "CustomerBin": paymentech.configuration.get("bin"),
            "CustomerMerchantId": paymentech.configuration.get("merchant")
        }
        payload = self.serialize(inject=authentication)
        result = service.request(payload)
        response = self.process_result(result)

        return response

    @staticmethod
    def process_result(result):
        result = ElementTree.fromstring(result)
        elements = result[0]

        dataset = {
            child.tag: child.text
            for child in elements
        }

        return dataset
