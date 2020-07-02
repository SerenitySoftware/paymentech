from paymentech.models.base import DataField, PaymentechModel


class Profile(PaymentechModel):
    customer_name = DataField("CustomerName", max_length=30)
    customer_reference_number = DataField("CustomerRefNum", max_length=22)
    customer_address1 = DataField("CustomerAddress1", max_length=30)
    customer_address2 = DataField("CustomerAddress2", max_length=30)
    customer_city = DataField("CustomerCity", max_length=20)
    customer_state = DataField("CustomerState", max_length=2)
    customer_zip = DataField("CustomerZIP", max_length=10)
    customer_email = DataField("CustomerEmail", max_length=50)
    customer_phone = DataField("CustomerPhone", max_length=14)
    customer_country_code = DataField("CustomerCountryCode", max_length=2)
    customer_profile_action = DataField("CustomerProfileAction", default="C", max_length=6)
    customer_profile_order_override = DataField("CustomerProfileOrderOverrideInd", max_length=2)
    customer_profile_from_order = DataField("CustomerProfileFromOrderInd", max_length=5)
    order_default_description = DataField("OrderDefaultDescription", max_length=64)
    order_default_amount = DataField("OrderDefaultAmount", max_length=12)
    customer_account_type = DataField("CustomerAccountType", default="CC", max_length=0)
    status = DataField("Status", default="A", max_length=2)
    card_number = DataField("CCAccountNum", max_length=22)
    card_expiration = DataField("CCExpireDate", max_length=6)
    bank_account_type = DataField("ECPAccountType", max_length=1)
    bank_account_number = DataField("ECPAccountDDA", max_length=17)
    bank_routing_number = DataField("ECPAccountRT", max_length=9)
    bank_payment_delivery_method = DataField("ECPBankPmtDlv", max_length=1)
    soft_descriptor_merchant = DataField("SDMerchantName", max_length=25)
    soft_descriptor_product = DataField("SDProductDescription", max_length=18)
    soft_descriptor_city = DataField("SDMerchantCity", max_length=13)
    soft_descriptor_phone = DataField("SDMerchantPhone", max_length=13)
    soft_descriptor_url = DataField("SDMerchantURL", max_length=13)
    soft_descriptor_email = DataField("SDMerchantEmail", max_length=13)
    biller_reference = DataField("BillerReferenceNumber", max_length=25)
    account_updater_eligibility = DataField("AccountUpdaterEligibility", default="Y", max_length=1)

    class Meta:
        wrapper = "Profile"
