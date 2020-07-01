from paymentech.models.base import DataField, PaymentechModel


class Order(PaymentechModel):
    industry_type = DataField("IndustryType")

    class Meta:
        wrapper = "NewOrder"
