from typing import Optional

from pydantic import Field

from paymentech.resources.base import PaymentechResource


class Inquiry(PaymentechResource):
    username: Optional[str] = Field(default=None, alias="OrbitalConnectionUsername")
    password: Optional[str] = Field(default=None, alias="OrbitalConnectionPassword")
    bin: Optional[str] = Field(default=None, alias="BIN")
    merchant_id: Optional[str] = Field(default=None, alias="MerchantID")
    terminal_id: Optional[str] = Field(alias="TerminalID", default="001", max_length=3)
    order_id: Optional[str] = Field(default=None, alias="OrderID", max_length=22)
    inquiry_retry_number: Optional[str] = Field(default=None, alias="InquiryRetryNumber", max_length=16)

    def authenticate(self, configuration):
        self.username = configuration.get("username")
        self.password = configuration.get("password")
        self.bin = configuration.get("bin")
        self.merchant_id = configuration.get("merchant_id")

    @property
    def wrapper(self):
        return "Inquiry"

    def query(self):
        return self.transact(validate=False)
