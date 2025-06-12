from typing import Optional

from pydantic import Field

from paymentech.resources.base import PaymentechResource


class MarkForCapture(PaymentechResource):
    username: Optional[str] = Field(default=None, alias="OrbitalConnectionUsername")
    password: Optional[str] = Field(default=None, alias="OrbitalConnectionPassword")
    order_id: Optional[str] = Field(default=None, alias="OrderID", max_length=22)
    amount: Optional[int] = Field(default=None, alias="Amount")
    bin: Optional[str] = Field(default=None, alias="BIN")
    merchant_id: Optional[str] = Field(default=None, alias="MerchantID")
    terminal_id: Optional[str] = Field(alias="TerminalID", default="001", max_length=3)
    transaction_reference_number: Optional[str] = Field(default=None, alias="TxRefNum", max_length=40)
    processing_status: Optional[str] = Field(default=None, alias="ProcStatus", max_length=6)
    approval_status: Optional[int] = Field(default=None, alias="ApprovalStatus")
    status_message: Optional[str] = Field(default=None, alias="StatusMsg")
    response_time: Optional[int] = Field(default=None, alias="RespTime")

    def authenticate(self, configuration):
        self.username = configuration.get("username")
        self.password = configuration.get("password")
        self.bin = configuration.get("bin")
        self.merchant_id = configuration.get("merchant_id")

    @property
    def wrapper(self):
        return "MarkForCapture"

    def capture(self, amount):
        self.amount = amount

        return self.transact()
