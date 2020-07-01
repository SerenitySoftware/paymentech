from paymentech.models import Order


def test_order_serialization():
    order = Order(industry_type="EC")
    result = order.serialize()

    assert result == "<NewOrder><IndustryType>EC</IndustryType></NewOrder>"
