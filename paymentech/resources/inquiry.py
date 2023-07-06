from typing import Optional

from pydantic import Field

from paymentech.resources.base import PaymentechResource


class Inquiry(PaymentechResource):
    username: Optional[str] = Field(alias="OrbitalConnectionUsername", default=None)
    password: Optional[str] = Field(alias="OrbitalConnectionPassword", default=None)
    bin: Optional[str] = Field(alias="BIN", default=None)
    merchant_id: Optional[str] = Field(alias="MerchantID", default=None)
    terminal_id: Optional[str] = Field(alias="TerminalID", default="001", max_length=3)
    order_id: Optional[str] = Field(alias="OrderID", default=None, max_length=22)
    inquiry_retry_number: Optional[str] = Field(alias="InquiryRetryNumber", default=None, max_length=16)

    def authenticate(self, configuration):
        self.username = configuration.get("username")
        self.password = configuration.get("password")
        self.bin = configuration.get("bin")
        self.merchant_id = configuration.get("merchant_id")

    class Config:
        wrapper = "Inquiry"

    def query(self):
        return self.transact(validate=False)
