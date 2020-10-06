class PaymentechException(Exception):

    def __init__(self, message, code=None, response=None):
        self.message = message
        self.code = code or 0
        self.response = response

    def __str__(self):
        return self.message
