from typing import Optional
from xml.etree import ElementTree

from pydantic import BaseModel, Field

import paymentech
from paymentech import service


class PaymentechResource(BaseModel):
    username: Optional[str] = Field(alias="OrbitalConnectionUsername")
    password: Optional[str] = Field(alias="OrbitalConnectionPassword")
    bin: Optional[str] = Field(alias="BIN")
    customer_bin: Optional[str] = Field(alias="CustomerBin")
    merchant_id: Optional[str] = Field(alias="CustomerMerchantId")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.username = paymentech.configuration.get("username")
        self.password = paymentech.configuration.get("password")
        self.bin = self.customer_bin = paymentech.configuration.get("bin")
        self.merchant_id = paymentech.configuration.get("merchant")

    def serialize(self):
        wrapper = self.__config__.wrapper

        payload = ElementTree.Element(wrapper)
        dataset = self.dict(by_alias=True)
        for key, value in dataset.items():
            if value is None:
                continue

            child = ElementTree.SubElement(payload, key)
            child.text = value

        return str(ElementTree.tostring(payload, 'unicode'))

    def transact(self):
        payload = self.serialize()
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
