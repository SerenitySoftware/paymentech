from .version import version


configuration = {
    "merchant_id": None,
    "bin": None,
    "username": None,
    "password": None,
    "environment": "test",
    "version": ""
}


def configure(merchant_id, bin, username, password, environment="test", **kwargs):
    configuration["merchant_id"] = merchant_id
    configuration["bin"] = bin
    configuration["username"] = username
    configuration["password"] = password
    configuration["environment"] = environment
    configuration["version"] = version

    if environment not in ["test", "production"]:
        raise ValueError("No environment named {0}".format(environment))

    configuration.update(kwargs)
