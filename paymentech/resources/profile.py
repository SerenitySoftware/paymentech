from typing import Optional

from pydantic import Field

from paymentech.resources.base import PaymentechResource


class Profile(PaymentechResource):
    username: Optional[str] = Field(default=None, alias="OrbitalConnectionUsername")
    password: Optional[str] = Field(default=None, alias="OrbitalConnectionPassword")
    customer_bin: Optional[str] = Field(default=None, alias="CustomerBin")
    merchant_id: Optional[str] = Field(default=None, alias="CustomerMerchantID")
    customer_name: Optional[str] = Field(default=None, alias="CustomerName", max_length=30)
    customer_reference_number: Optional[str] = Field(default=None, alias="CustomerRefNum", max_length=22)
    customer_address1: Optional[str] = Field(default=None, alias="CustomerAddress1", max_length=30)
    customer_address2: Optional[str] = Field(default=None, alias="CustomerAddress2", max_length=30)
    customer_city: Optional[str] = Field(default=None, alias="CustomerCity", max_length=20)
    customer_state: Optional[str] = Field(default=None, alias="CustomerState", max_length=2)
    customer_zip: Optional[str] = Field(default=None, alias="CustomerZIP", max_length=10)
    customer_email: Optional[str] = Field(default=None, alias="CustomerEmail", max_length=50)
    customer_phone: Optional[str] = Field(default=None, alias="CustomerPhone", max_length=14)
    customer_country_code: Optional[str] = Field(alias="CustomerCountryCode", default="US", max_length=2)
    customer_profile_action: Optional[str] = Field(alias="CustomerProfileAction", default="C", max_length=6)
    customer_profile_order_override: Optional[str] = Field(
        alias="CustomerProfileOrderOverrideInd", default="NO", max_length=2
    )
    customer_profile_from_order: Optional[str] = Field(alias="CustomerProfileFromOrderInd", default="A", max_length=5)
    order_default_description: Optional[str] = Field(default=None, alias="OrderDefaultDescription", max_length=64)
    order_default_amount: Optional[str] = Field(default=None, alias="OrderDefaultAmount", max_length=12)
    customer_account_type: Optional[str] = Field(alias="CustomerAccountType", default="CC", max_length=0)
    status: Optional[str] = Field(default=None, alias="Status", max_length=2)
    card_number: Optional[str] = Field(default=None, alias="CCAccountNum", max_length=22)
    card_expiration: Optional[str] = Field(default=None, alias="CCExpireDate", max_length=6)
    bank_account_number: Optional[str] = Field(default=None, alias="ECPAccountDDA", max_length=17)
    bank_account_type: Optional[str] = Field(default=None, alias="ECPAccountType", max_length=1)
    bank_routing_number: Optional[str] = Field(default=None, alias="ECPAccountRT", max_length=9)
    bank_payment_delivery_method: Optional[str] = Field(default=None, alias="ECPBankPmtDlv", max_length=1)
    soft_descriptor_merchant: Optional[str] = Field(default=None, alias="SDMerchantName", max_length=25)
    soft_descriptor_product: Optional[str] = Field(default=None, alias="SDProductDescription", max_length=18)
    soft_descriptor_city: Optional[str] = Field(default=None, alias="SDMerchantCity", max_length=13)
    soft_descriptor_phone: Optional[str] = Field(default=None, alias="SDMerchantPhone", max_length=13)
    soft_descriptor_url: Optional[str] = Field(default=None, alias="SDMerchantURL", max_length=13)
    soft_descriptor_email: Optional[str] = Field(default=None, alias="SDMerchantEmail", max_length=13)
    biller_reference: Optional[str] = Field(default=None, alias="BillerReferenceNumber", max_length=25)
    account_updater_eligibility: Optional[str] = Field(default=None, alias="AccountUpdaterEligibility", max_length=1)
    card_brand: Optional[str] = Field(default=None, alias="CardBrand", max_length=22)
    mit_message_type: Optional[str] = Field(default=None, alias="MITMsgType", max_length=4)
    mit_submitted_transaction_id: Optional[str] = Field(default=None, alias="MITSubmittedTransactionID", max_length=15)

    @property
    def wrapper(self):
        return "Profile"

    def authenticate(self, configuration):
        self.username = configuration.get("username")
        self.password = configuration.get("password")
        self.customer_bin = configuration.get("bin")
        self.merchant_id = configuration.get("merchant_id")

    def create(self):
        self.customer_profile_action = "C"
        return self.transact()

    def read(self):
        self.validate_customer_reference_number("read")
        self.customer_profile_action = "R"

        return self.transact(
            include={
                "customer_profile_action",
                "customer_reference_number",
                "customer_bin",
            }
        )

    def update(self):
        self.validate_customer_reference_number("update")
        self.customer_profile_action = "U"

        return self.transact()

    def delete(self):
        self.validate_customer_reference_number("delete")
        self.customer_profile_action = "D"
        self.customer_account_type = None
        self.customer_profile_order_override = None
        self.customer_profile_from_order = None

        return self.transact()

    def validate_customer_reference_number(self, action="read"):
        if not self.customer_reference_number:
            raise ValueError(f"Set the customer_reference_number to {action} a profile")
