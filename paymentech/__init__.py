import pathlib


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

    if environment not in ["test", "production"]:
        raise ValueError("No environment named {0}".format(environment))

    version_file_path = pathlib.Path(__file__).parent.parent.absolute() / "VERSION"
    with open(version_file_path, "r") as version_file:
        configuration["version"] = version_file.read().strip()

    configuration.update(kwargs)
