class PaymentechException(Exception):

    def __init__(self, message, code=None):
        self.message = message
        self.code = code or 0

    def __str__(self):
        return self.message
