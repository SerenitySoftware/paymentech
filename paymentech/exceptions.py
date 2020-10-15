class PaymentechException(Exception):

    def __init__(self, message, category=None, code=None, response=None):
        self.message = message
        self.category = category or None
        self.code = code or 0
        self.response = response

    def __str__(self):
        return self.message
