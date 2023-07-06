from typing import Optional
import uuid

from pydantic import Field

from paymentech import exceptions
from paymentech.resources.authorization import MarkForCapture
from paymentech.resources.base import PaymentechResource
from paymentech.resources.reversal import Reversal


class Order(PaymentechResource):
    username: Optional[str] = Field(alias="OrbitalConnectionUsername", default=None)
    password: Optional[str] = Field(alias="OrbitalConnectionPassword", default=None)
    industry_type: Optional[str] = Field(alias="IndustryType", default="EC", max_length=2)
    message_type: Optional[str] = Field(alias="MessageType", default=None, max_length=2)
    bin: Optional[str] = Field(alias="BIN", default=None)
    merchant_id: Optional[str] = Field(alias="MerchantID", default=None)
    terminal_id: Optional[str] = Field(alias="TerminalID", default="001", max_length=3)
    card_brand: Optional[str] = Field(alias="CardBrand", default=None, max_length=2)
    payment_action: Optional[str] = Field(alias="PaymentActionInd", default=None, max_length=1)
    account_number: Optional[str] = Field(alias="AccountNum", default=None, max_length=19)
    expiration: Optional[str] = Field(alias="Exp", default=None, max_length=6)
    currency_code: Optional[str] = Field(alias="CurrencyCode", default="840", max_length=3)
    currency_exponent: Optional[str] = Field(alias="CurrencyExponent", default="2", max_length=6)
    card_security_indicator: Optional[str] = Field(alias="CardSecValInd", default=None, max_length=1)
    card_security_value: Optional[str] = Field(alias="CardSecVal", default=None, max_length=4)
    bank_routing_number: Optional[str] = Field(alias="BCRtNum", default=None, max_length=9)
    check_dda: Optional[str] = Field(alias="CheckDDA", default=None, max_length=17)
    bank_account_type: Optional[str] = Field(alias="BankAccountType", default=None, max_length=1)
    ecp_authorization_method: Optional[str] = Field(alias="ECPAuthMethod", default=None, max_length=1)
    ecp_payment_delivery_method: Optional[str] = Field(alias="BankPmtDelv", default=None, max_length=1)
    ecp_action_code: Optional[str] = Field(alias="ECPActionCode", default=None, max_length=2)
    ecp_check_serial_number: Optional[str] = Field(alias="ECPCheckSerialNumber", default=None, max_length=9)
    ecp_terminal_city: Optional[str] = Field(alias="ECPTerminalCity", default=None, max_length=4)
    ecp_terminal_state: Optional[str] = Field(alias="ECPTerminalState", default=None, max_length=2)
    ecp_image_reference: Optional[str] = Field(alias="ECPImageReferenceNumber", default=None, max_length=32)
    customer_email: Optional[str] = Field(alias="CustomerEmail", default=None, max_length=50)
    customer_email_type: Optional[str] = Field(alias="EmailAddressSubtype", default=None, max_length=1)
    customer_browser_name: Optional[str] = Field(alias="CustomerBrowserName", default=None, max_length=60)
    customer_ip_address: Optional[str] = Field(alias="CustomerIpAddress", default=None, max_length=45)
    zip: Optional[str] = Field(alias="AVSzip", default=None, max_length=10)
    address1: Optional[str] = Field(alias="AVSaddress1", default=None, max_length=30)
    address2: Optional[str] = Field(alias="AVSaddress2", default=None, max_length=30)
    city: Optional[str] = Field(alias="AVScity", default=None, max_length=20)
    state: Optional[str] = Field(alias="AVSstate", default=None, max_length=2)
    phone_number: Optional[str] = Field(alias="AVSphoneNum", default=None, max_length=14)
    cardholder_name: Optional[str] = Field(alias="AVSname", default=None)
    phone_number_type: Optional[str] = Field(alias="AVSPhoneType", default=None, max_length=1)
    country_code: Optional[str] = Field(alias="AVScountryCode", default=None, max_length=2)
    shipping_method: Optional[str] = Field(alias="ShippingMethod", default=None, max_length=1)
    customer_profile_method: Optional[str] = Field(alias="CustomerProfileFromOrderInd", default=None, max_length=5)
    customer_reference_number: Optional[str] = Field(alias="CustomerRefNum", default=None, max_length=22)
    customer_automatic_number_identification: Optional[str] = Field(alias="CustomerAni", default=None, max_length=10)
    customer_profile_order_override_method: Optional[str] = Field(
        alias="CustomerProfileOrderOverrideInd", default=None, max_length=2
    )
    customer_token_indicator: Optional[str] = Field(alias="DPANInd", default=None, max_length=1)
    status: Optional[str] = Field(alias="Status", default=None, max_length=2)
    authentication_eci_indicator: Optional[str] = Field(alias="AuthenticationECIInd", default=None, max_length=2)
    cavv: Optional[str] = Field(alias="CAVV", default=None, max_length=70)
    aav: Optional[str] = Field(alias="AAV", default=None, max_length=32)
    xid: Optional[str] = Field(alias="XID", default=None, max_length=40)
    aevv: Optional[str] = Field(alias="AEVV", default=None, max_length=56)
    prior_authorization_identifier: Optional[str] = Field(alias="PriorAuthID", default=None, max_length=6)
    comments: Optional[str] = Field(alias="Comments", default=None, max_length=256)
    shipping_reference: Optional[str] = Field(alias="ShippingRef", default=None, max_length=40)
    tax_type: Optional[str] = Field(alias="TaxInd", default=None, max_length=1)
    tax: Optional[str] = Field(alias="Tax", default=None, max_length=12)
    soft_descriptor_merchant: Optional[str] = Field(alias="SDMerchantName", default=None, max_length=25)
    soft_descriptor_product: Optional[str] = Field(alias="SDProductDescription", default=None, max_length=18)
    soft_descriptor_city: Optional[str] = Field(alias="SDMerchantCity", default=None, max_length=13)
    soft_descriptor_phone: Optional[str] = Field(alias="SDMerchantPhone", default=None, max_length=13)
    soft_descriptor_url: Optional[str] = Field(alias="SDMerchantURL", default=None, max_length=13)
    soft_descriptor_email: Optional[str] = Field(alias="SDMerchantEmail", default=None, max_length=13)
    recurring_indicator: Optional[str] = Field(alias="RecurringInd", default=None, max_length=2)
    euro_debit_country_code: Optional[str] = Field(alias="EUDDCountryCode", default=None, max_length=2)
    euro_debit_bank_sort_code: Optional[str] = Field(alias="EUDDBankSortCode", default=None, max_length=10)
    euro_debit_rib: Optional[str] = Field(alias="EUDDRibCode", default=None, max_length=2)
    biller_reference: Optional[str] = Field(alias="BillerReferenceNumber", default=None, max_length=25)
    managed_billing_type: Optional[str] = Field(alias="MBType", default=None, max_length=1)
    managed_billing_order_id_generation_method: Optional[str] = Field(
        alias="MBOrderIdGenerationMethod", default=None, max_length=2
    )
    managed_billing_start_date: Optional[str] = Field(alias="MBRecurringStartDate", default=None, max_length=8)
    managed_billing_end_date: Optional[str] = Field(alias="MBRecurringEndDate", default=None, max_length=8)
    managed_billing_no_end_date: Optional[str] = Field(alias="MBRecurringNoEndDateFlag", default=None, max_length=1)
    managed_billing_max_billings: Optional[str] = Field(alias="MBRecurringMaxBillings", default=None, max_length=6)
    managed_billing_frequency: Optional[str] = Field(alias="MBRecurringFrequency", default=None, max_length=64)
    managed_billing_deferred_bill_date: Optional[str] = Field(alias="MBDeferredBillDate", default=None, max_length=8)
    order_id: Optional[str] = Field(alias="OrderID", default=None, max_length=22)
    amount: Optional[int] = Field(alias="Amount", default=None)
    transaction_reference_number: Optional[str] = Field(alias="TxRefNum", default=None, max_length=40)
    partial_auth_indicator: Optional[str] = Field(alias="PartialAuthInd", default=None, max_length=1)
    account_updater_eligibility: Optional[str] = Field(alias="AccountUpdaterEligibility", default=None, max_length=1)
    use_stored_aav_indicator: Optional[str] = Field(alias="UseStoredAAVInd", default=None, max_length=1)
    mit_message_type: Optional[str] = Field(alias="MITMsgType", default=None, max_length=4)
    mit_stored_credential_indicator: Optional[str] = Field(alias="MITStoredCredentialInd", default=None, max_length=1)
    # NOTE: Skipping all Level 3 transaction elements and a significant number of other elements for now

    class Config:
        wrapper = "NewOrder"

    def authenticate(self, configuration):
        self.username = configuration.get("username")
        self.password = configuration.get("password")
        self.bin = configuration.get("bin")
        self.merchant_id = configuration.get("merchant_id")

    def generate_order_id(self):
        self.order_id = self.order_id or uuid.uuid4().node

    def authorize(self):
        self.message_type = "A"
        self.generate_order_id()
        return self.transact()

    def authorize_and_capture(self):
        self.message_type = "AC"
        self.generate_order_id()
        return self.transact()

    def capture(self, amount=None):
        mark_for_capture = MarkForCapture(
            order_id=self.order_id,
            transaction_reference_number=self.transaction_reference_number
        )
        amount = amount or self.amount
        if not amount or amount < 0:
            raise exceptions.PaymentechException("Captured amount must be greater than zero", "validation")

        return mark_for_capture.capture(amount)

    def generate(self):
        self.message_type = "AC"
        self.generate_order_id()
        return self.transact()

    def refund(self):
        self.message_type = "R"
        if not self.order_id and not self.transaction_reference_number:
            self.generate_order_id()

        return self.transact()

    def reverse(self, amount=None):
        reversal = Reversal(
            order_id=self.order_id,
            transaction_reference_number=self.transaction_reference_number
        )

        return reversal.reverse(amount)
