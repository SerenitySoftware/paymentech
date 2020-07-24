from typing import Optional
from xml.dom import minidom
from xml.etree import ElementTree

from pydantic import BaseModel, Field

import paymentech
from paymentech import service


class PaymentechResource(BaseModel):
    username: Optional[str] = Field(alias="OrbitalConnectionUsername")
    password: Optional[str] = Field(alias="OrbitalConnectionPassword")
    bin: Optional[str] = Field(alias="BIN")
    customer_bin: Optional[str] = Field(alias="CustomerBin")
    merchant_id: Optional[str] = Field(alias="CustomerMerchantID")

    def __init__(self, **data):
        super().__init__(**data)
        self.assign(data)

    def serialize(self):
        self.username = paymentech.configuration.get("username")
        self.password = paymentech.configuration.get("password")
        self.bin = self.customer_bin = paymentech.configuration.get("bin")
        self.merchant_id = paymentech.configuration.get("merchant_id")

        payload = ElementTree.Element("Request")
        wrapper = ElementTree.SubElement(payload, self.__config__.wrapper)
        dataset = self.dict(by_alias=True)
        for key, value in dataset.items():
            if key in getattr(self.__config__, "skip", []):
                continue

            if value is None:
                continue

            child = ElementTree.SubElement(wrapper, key)
            child.text = value

        payload = ElementTree.tostring(payload, 'unicode')
        payload = minidom.parseString(payload)
        payload = payload.toprettyxml(indent="  ", encoding="UTF-8")

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

        response = self.__config__.response()
        return response.assign(dataset)

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
