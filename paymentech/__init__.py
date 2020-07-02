configuration = {
    "merchant_id": None,
    "bin": None,
    "username": None,
    "password": None
}


def configure(merchant_id, bin, username, password, **kwargs):
    configuration["merchant_id"] = merchant_id
    configuration["bin"] = bin
    configuration["username"] = username
    configuration["password"] = password

    configuration.update(kwargs)
