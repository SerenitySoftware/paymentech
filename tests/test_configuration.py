import paymentech


def test_configuration():
    paymentech.configure("user", "pass", "1", "pns")

    assert paymentech.configuration.get("merchant_id") == "1"
    assert paymentech.configuration.get("bin") == "000002"
    assert paymentech.configuration.get("username") == "user"
    assert paymentech.configuration.get("password") == "pass"


def test_platforms():
    paymentech.configure("user", "pass", "1", "stratus")
    assert paymentech.configuration.get("bin") == "000001"

    paymentech.configure("user", "pass", "1", "pns")
    assert paymentech.configuration.get("bin") == "000002"

    paymentech.configure("user", "pass", "1", "garbage")
    assert paymentech.configuration.get("bin") == "000002"


def test_configuration_with_additional_options():
    paymentech.configure("user", "pass", "1", "stratus", something="extra")

    assert paymentech.configuration.get("something", None) == "extra"
