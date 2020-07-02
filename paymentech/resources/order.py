from paymentech.resources import fields
from paymentech.resources.base import PaymentechResource


class Order(PaymentechResource):
    order_id = fields.DataField("OrderID", max_length=22)
    industry_type = fields.DataField("IndustryType", default="EC", max_length=2)
    message_type = fields.DataField("MessageType", default="AC", max_length=2)
    payment_action = fields.DataField("PaymentActionInd", max_length=1)
    terminal_id = fields.DataField("TerminalID", default="001", max_length=3)
    card_brand = fields.DataField("CardBrand", max_length=2)
    account_number = fields.DataField("AccountNum", max_length=19)
    expiration = fields.DataField("Exp", max_length=6)
    currency_code = fields.DataField("CurrencyCode", default="840", max_length=3)
    currency_exponent = fields.DataField("CurrencyExponent", default="2", max_length=6)
    card_security_indicator = fields.DataField("CardSecValInd", max_length=1)
    card_security_value = fields.DataField("CardSecVal", max_length=4)
    bank_routing_number = fields.DataField("BCRtNum", max_length=9)
    check_dda = fields.DataField("CheckDDA", max_length=17)
    bank_account_type = fields.DataField("BankAccountType", max_length=1)
    ecp_authorization_method = fields.DataField("ECPAuthMethod", default="I", max_length=1)
    ecp_payment_delivery_method = fields.DataField("BankPmtDelv", default="B", max_length=1)
    ecp_action_code = fields.DataField("ECPActionCode", max_length=2)
    ecp_check_serial_number = fields.DataField("ECPCheckSerialNumber", max_length=9)
    ecp_terminal_city = fields.DataField("ECPTerminalCity", max_length=4)
    ecp_terminal_state = fields.DataField("ECPTerminalState", max_length=2)
    ecp_image_reference = fields.DataField("ECPImageReferenceNumber", max_length=32)
    customer_email = fields.DataField("CustomerEmail", max_length=50)
    customer_email_type = fields.DataField("EmailAddressSubtype", max_length=1)
    customer_browser_name = fields.DataField("CustomerBrowserName", max_length=60)
    customer_ip_address = fields.DataField("CustomerIpAddress", max_length=45)
    address1 = fields.DataField("AVSaddress1", max_length=30)
    address2 = fields.DataField("AVSaddress2", max_length=30)
    city = fields.DataField("AVScity", max_length=20)
    state = fields.DataField("AVSstate", max_length=2)
    zip = fields.DataField("AVSzip", max_length=10)
    phone_number = fields.DataField("AVSphoneNum", max_length=14)
    phone_number_type = fields.DataField("AVSPhoneType", max_length=1)
    cardholder_name = fields.DataField("AVSname")
    country_code = fields.DataField("AVScountryCode", default="US", max_length=2)
    shipping_method = fields.DataField("ShippingMethod", max_length=1)
    destination_zip = fields.DataField("AVSDestzip", max_length=10)
    destination_address1 = fields.DataField("AVSDestzip", max_length=30)
    destination_address2 = fields.DataField("AVSDestaddress2", max_length=28)
    destination_city = fields.DataField("AVSDestcity", max_length=20)
    destination_state = fields.DataField("AVSDeststate", max_length=2)
    destination_phone_number = fields.DataField("AVSDestphoneNum", max_length=14)
    destination_phone_type = fields.DataField("AVSDestPhoneType", max_length=1)
    destination_name = fields.DataField("AVSDestname", max_length=30)
    destination_country_code = fields.DataField("AVSDestcountryCode", default="US", max_length=2)
    customer_profile_method = fields.DataField("CustomerProfileFromOrderInd", max_length=5)
    customer_reference_number = fields.DataField("CustomerRefNum", max_length=22)
    customer_automatic_number_identification = fields.DataField("CustomerAni", max_length=10)
    customer_profile_order_override_method = fields.DataField(
        "CustomerProfileOrderOverrideInd", default="NO", max_length=2
    )
    customer_token_indicator = fields.DataField("DPANInd", max_length=1)
    status = fields.DataField("Status", max_length=2)
    authentication_eci_indicator = fields.DataField("AuthenticationECIInd", max_length=2)
    cavv = fields.DataField("CAVV", max_length=70)
    aav = fields.DataField("AAV", max_length=32)
    xid = fields.DataField("XID", max_length=40)
    aevv = fields.DataField("AEVV", max_length=56)
    prior_authorization_identifier = fields.DataField("PriorAuthID", max_length=6)
    amount = fields.DataField("Amount", max_length=12)
    comments = fields.DataField("Comments", max_length=256)
    shipping_reference = fields.DataField("ShippingRef", max_length=40)
    tax_type = fields.DataField("TaxInd", max_length=1)
    tax = fields.DataField("Tax", max_length=12)
    amex_transaction_advice_addendum1 = fields.DataField("AMEXTranAdvAddn1", max_length=40)
    amex_transaction_advice_addendum2 = fields.DataField("AMEXTranAdvAddn2", max_length=40)
    amex_transaction_advice_addendum3 = fields.DataField("AMEXTranAdvAddn3", max_length=40)
    amex_transaction_advice_addendum4 = fields.DataField("AMEXTranAdvAddn4", max_length=40)
    soft_descriptor_merchant = fields.DataField("SDMerchantName", max_length=25)
    soft_descriptor_product = fields.DataField("SDProductDescription", max_length=18)
    soft_descriptor_city = fields.DataField("SDMerchantCity", max_length=13)
    soft_descriptor_phone = fields.DataField("SDMerchantPhone", max_length=13)
    soft_descriptor_url = fields.DataField("SDMerchantURL", max_length=13)
    soft_descriptor_email = fields.DataField("SDMerchantEmail", max_length=13)
    recurring_indicator = fields.DataField("RecurringInd", max_length=2)
    euro_debit_country_code = fields.DataField("EUDDCountryCode", max_length=2)
    euro_debit_bank_sort_code = fields.DataField("EUDDBankSortCode", max_length=10)
    euro_debit_rib = fields.DataField("EUDDRibCode", max_length=2)
    biller_reference = fields.DataField("BillerReferenceNumber", max_length=25)
    managed_billing_type = fields.DataField("MBType", max_length=1)
    managed_billing_order_id_generation_method = fields.DataField("MBOrderIdGenerationMethod", max_length=2)
    managed_billing_start_date = fields.DataField("MBRecurringStartDate", max_length=8)
    managed_billing_end_date = fields.DataField("MBRecurringEndDate", max_length=8)
    managed_billing_no_end_date = fields.DataField("MBRecurringNoEndDateFlag", max_length=1)
    managed_billing_max_billings = fields.DataField("MBRecurringMaxBillings", max_length=6)
    managed_billing_frequency = fields.DataField("MBRecurringFrequency", max_length=64)
    managed_billing_deferred_bill_date = fields.DataField("MBDeferredBillDate", max_length=8)
    transaction_reference_number = fields.DataField("TxRefNum", max_length=40)
    purchase_order_number = fields.DataField("PCOrderNum", max_length=17)
    purchase_order_name = fields.DataField("PCDestName", max_length=30)
    purchase_order_address1 = fields.DataField("PCDestAddress1", max_length=30)
    purchase_order_address2 = fields.DataField("PCDestAddress2", max_length=30)
    purchase_order_city = fields.DataField("PCDestCity", max_length=20)
    purchase_order_state = fields.DataField("PCDestState", max_length=2)
    purchase_order_zip = fields.DataField("PCDestZip", max_length=10)
    partial_auth_indicator = fields.DataField("PartialAuthInd", max_length=1)
    account_updater_eligibility = fields.DataField("AccountUpdaterEligibility", default="Y", max_length=1)
    use_stored_aav_indicator = fields.DataField("UseStoredAAVInd", max_length=1)
    # NOTE: Skipping all Level 3 transaction elements and a significant number of other elements for now

    class Meta:
        wrapper = "NewOrder"
