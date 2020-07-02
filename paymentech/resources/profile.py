from paymentech.resources import fields
from paymentech.resources.base import PaymentechResource


class Profile(PaymentechResource):
    customer_name = fields.DataField("CustomerName", max_length=30)
    customer_reference_number = fields.DataField("CustomerRefNum", max_length=22)
    customer_address1 = fields.DataField("CustomerAddress1", max_length=30)
    customer_address2 = fields.DataField("CustomerAddress2", max_length=30)
    customer_city = fields.DataField("CustomerCity", max_length=20)
    customer_state = fields.DataField("CustomerState", max_length=2)
    customer_zip = fields.DataField("CustomerZIP", max_length=10)
    customer_email = fields.DataField("CustomerEmail", max_length=50)
    customer_phone = fields.DataField("CustomerPhone", max_length=14)
    customer_country_code = fields.DataField("CustomerCountryCode", max_length=2)
    customer_profile_action = fields.DataField("CustomerProfileAction", default="C", max_length=6)
    customer_profile_order_override = fields.DataField("CustomerProfileOrderOverrideInd", max_length=2)
    customer_profile_from_order = fields.DataField("CustomerProfileFromOrderInd", max_length=5)
    order_default_description = fields.DataField("OrderDefaultDescription", max_length=64)
    order_default_amount = fields.DataField("OrderDefaultAmount", max_length=12)
    customer_account_type = fields.DataField("CustomerAccountType", default="CC", max_length=0)
    status = fields.DataField("Status", default="A", max_length=2)
    card_number = fields.DataField("CCAccountNum", max_length=22)
    card_expiration = fields.DataField("CCExpireDate", max_length=6)
    bank_account_type = fields.DataField("ECPAccountType", max_length=1)
    bank_account_number = fields.DataField("ECPAccountDDA", max_length=17)
    bank_routing_number = fields.DataField("ECPAccountRT", max_length=9)
    bank_payment_delivery_method = fields.DataField("ECPBankPmtDlv", max_length=1)
    soft_descriptor_merchant = fields.DataField("SDMerchantName", max_length=25)
    soft_descriptor_product = fields.DataField("SDProductDescription", max_length=18)
    soft_descriptor_city = fields.DataField("SDMerchantCity", max_length=13)
    soft_descriptor_phone = fields.DataField("SDMerchantPhone", max_length=13)
    soft_descriptor_url = fields.DataField("SDMerchantURL", max_length=13)
    soft_descriptor_email = fields.DataField("SDMerchantEmail", max_length=13)
    biller_reference = fields.DataField("BillerReferenceNumber", max_length=25)
    account_updater_eligibility = fields.DataField("AccountUpdaterEligibility", default="Y", max_length=1)

    class Meta:
        wrapper = "Profile"
