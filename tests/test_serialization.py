import re

from paymentech.models import Order


def test_order_serialization():
    order = Order(industry_type="EC")
    result = order.serialize()

    expected = """
        <NewOrder>
            <IndustryType>EC</IndustryType>
            <MessageType>AC</MessageType>
            <TerminalID>001</TerminalID>
            <CurrencyCode>840</CurrencyCode>
            <CurrencyExponent>2</CurrencyExponent>
            <ECPAuthMethod>I</ECPAuthMethod>
            <BankPmtDelv>B</BankPmtDelv>
            <AVScountryCode>US</AVScountryCode>
            <AVSDestcountryCode>US</AVSDestcountryCode>
            <CustomerProfileOrderOverrideInd>NO</CustomerProfileOrderOverrideInd>
            <AccountUpdaterEligibility>Y</AccountUpdaterEligibility>
        </NewOrder>
    """
    # Trim out the whitespace
    expected = re.sub(r'\s+', '', expected)

    assert result == expected
