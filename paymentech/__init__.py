from .version import version


configuration = {
    "merchant_id": None,
    "bin": None,
    "username": None,
    "password": None,
    "environment": "test",
    "version": ""
}


def configure(username, password, merchant_id, platform="pns", environment="test", **kwargs):
    platform_bins = {
        "stratus": "000001",
        "pns": "000002"
    }

    configuration["merchant_id"] = merchant_id
    configuration["bin"] = platform_bins.get(platform.lower(), platform_bins["pns"])
    configuration["username"] = username
    configuration["password"] = password
    configuration["environment"] = environment
    configuration["version"] = version

    if environment not in ["test", "production"]:
        raise ValueError(f"No environment named {environment}")

    configuration.update(kwargs)
