from xml.dom import minidom
from xml.etree import ElementTree

from pydantic import BaseModel

import paymentech
from paymentech import exceptions, service


class PaymentechResource(BaseModel):

    def __init__(self, **data):
        super().__init__(**data)
        self.assign(data)

    def authenticate(self, configuration):
        raise NotImplementedError()

    @staticmethod
    def prettify(text):
        payload = minidom.parseString(text)
        payload = payload.toprettyxml(indent="    ", encoding="UTF-8").decode("utf-8")

        return payload

    def serialize(self):
        self.authenticate(paymentech.configuration)

        payload = ElementTree.Element("Request")
        wrapper = ElementTree.SubElement(payload, self.__config__.wrapper)
        dataset = self.dict(by_alias=True)
        for key, value in dataset.items():
            if value is None:
                continue

            child = ElementTree.SubElement(wrapper, key)
            child.text = str(value)

        payload = ElementTree.tostring(payload, 'unicode')
        payload = self.prettify(payload)

        return payload

    def transact(self):
        payload = self.serialize()
        trace, result = service.request(payload)
        dataset = self.process_result(result)

        self.validate_response(dataset)
        self.assign(dataset)
        self.set_last_trace(trace)

        return result

    def set_last_trace(self, trace):
        self.__config__.trace = trace

    def get_last_trace(self):
        try:
            return self.__config__.trace
        except Exception:
            pass

        return None

    @staticmethod
    def validate_response(result):
        message = result.get("StatusMsg", result.get("RespMsg", "Error"))
        proc_status = result.get("ProcStatus", None)
        if proc_status not in (None, 0, "0", "00"):
            raise exceptions.PaymentechException(message, proc_status)

        approval_status = result.get("ApprovalStatus", None)
        if approval_status in (0, "0"):
            message = message or "Payment declined"
            raise exceptions.PaymentechException(message, approval_status)

        if approval_status in (2, "2"):
            message = message or "System error, please try again"
            raise exceptions.PaymentechException(message, approval_status)

        cvv_resp_code = result.get("CVV2RespCode", None)
        if cvv_resp_code in ("N", "S", "I", "Y"):
            cvv_lookup = {
                "N": "CVV doesn't match",
                "S": "CVV is missing",
                "I": "Invalid CVV",
                "Y": "Invalid CVV"
            }

            message = cvv_lookup.get(cvv_resp_code)
            raise exceptions.PaymentechException(message, cvv_resp_code)

        profile_proc_status = result.get("ProfileProcStatus", None)
        if profile_proc_status not in (None, 0, "0", "00"):
            message = result.get("CustomerProfileMessage", message)
            raise exceptions.PaymentechException(message, profile_proc_status)

    @staticmethod
    def process_result(result):
        result = ElementTree.fromstring(result)
        elements = result[0]

        dataset = {child.tag: child.text for child in elements}

        return dataset

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
