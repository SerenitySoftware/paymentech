import paymentech


def test_configuration():
    paymentech.configure("1", "2", "user", "pass")

    assert paymentech.configuration.get("merchant_id") == "1"
    assert paymentech.configuration.get("bin") == "2"
    assert paymentech.configuration.get("username") == "user"
    assert paymentech.configuration.get("password") == "pass"


def test_configuration_with_additional_options():
    paymentech.configure("1", "2", "user", "pass", something="extra")

    assert paymentech.configuration.get("something", None) == "extra"
