from typing import Optional

from pydantic import Field

from paymentech.resources.base import PaymentechResource


class Reversal(PaymentechResource):
    username: Optional[str] = Field(alias="OrbitalConnectionUsername")
    password: Optional[str] = Field(alias="OrbitalConnectionPassword")
    transaction_reference_number: Optional[str] = Field(alias="TxRefNum", max_length=40)
    transaction_reference_index: Optional[int] = Field(alias="TxRefIdx")
    amount: Optional[int] = Field(alias="AdjustedAmt")
    outstanding: Optional[int] = Field(alias="OutstandingAmt")
    order_id: Optional[str] = Field(alias="OrderID", max_length=22)
    bin: Optional[str] = Field(alias="BIN")
    merchant_id: Optional[str] = Field(alias="MerchantID")
    terminal_id: Optional[str] = Field(alias="TerminalID", default="001", max_length=3)
    processing_status: Optional[str] = Field(alias="ProcStatus", max_length=6)
    approval_status: Optional[int] = Field(alias="ApprovalStatus")
    status_message: Optional[str] = Field(alias="StatusMsg")
    response_time: Optional[int] = Field(alias="RespTime")

    def authenticate(self, configuration):
        self.username = configuration.get("username")
        self.password = configuration.get("password")
        self.bin = configuration.get("bin")
        self.merchant_id = configuration.get("merchant_id")

    class Config:
        wrapper = "Reversal"

    def reverse(self, amount=None):
        if amount:
            self.amount = amount

        return self.transact()
