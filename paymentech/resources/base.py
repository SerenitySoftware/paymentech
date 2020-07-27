from xml.dom import minidom
from xml.etree import ElementTree

from pydantic import BaseModel

import paymentech
from paymentech import service


class PaymentechResource(BaseModel):

    def __init__(self, **data):
        super().__init__(**data)
        self.assign(data)

    def authenticate(self, configuration):
        raise NotImplementedError()

    def prettify(self, text):
        payload = minidom.parseString(text)
        payload = payload.toprettyxml(indent="    ", encoding="UTF-8").decode("utf-8")

        return payload

    def serialize(self):
        self.authenticate(paymentech.configuration)

        payload = ElementTree.Element("Request")
        wrapper = ElementTree.SubElement(payload, self.__config__.wrapper)
        dataset = self.dict(by_alias=True)
        for key, value in dataset.items():
            if key in getattr(self.__config__, "skip", []):
                continue

            if value is None:
                continue

            child = ElementTree.SubElement(wrapper, key)
            child.text = str(value)

        payload = ElementTree.tostring(payload, 'unicode')
        payload = self.prettify(payload)

        return payload

    def transact(self):
        payload = self.serialize()
        result = service.request(payload)
        response = self.process_result(result)

        return response

    def process_result(self, result):
        result = ElementTree.fromstring(result)
        elements = result[0]

        dataset = {child.tag: child.text for child in elements}

        return self.assign(dataset)

    def assign(self, dataset):
        dataset = dataset or {}

        for field, value in self.__dict__.items():
            if field not in self.__fields__:
                continue

            alias = self.__fields__[field].alias
            if alias not in dataset and field not in dataset:
                continue

            result_value = dataset.get(alias, dataset.get(field))
            setattr(self, field, result_value)

        return self
