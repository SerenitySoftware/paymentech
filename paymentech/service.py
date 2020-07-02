import random
import time

import requests

import paymentech


endpoints = {
    "test": ["https://orbitalvar1.chasepaymentech.com", "https://orbitalvar2.chasepaymentech.com"],
    "production": ["https://orbital1.chasepaymentech.com", "https://orbital2.chasepaymentech.com"]
}


def request(payload):
    environment = paymentech.configuration.get("environment")
    maximum_attempts = paymentech.configuration.get("attempts", 3)
    urls = endpoints[environment]
    trace = random.randint(1, 9999999999999999)

    headers = {
        "MIME-Version": "1.1",
        "Content-type": "application/PTI80",
        "Content-transfer-encoding": "text",
        "Request-Number": "1",
        "Document-type": "Request",
        "Trace-Number": trace,
        "Interface-Version": "Chase Paymentech Python SDK/{0}".format(paymentech.configuration.get("version"))
    }

    for url in urls:
        for attempt in range(maximum_attempts):
            try:
                response = requests.post(url, data=payload, headers=headers)

                if response and response.text:
                    return response.text
            except Exception:
                pass

            # Avoid throttling
            time.sleep(0.5)

    raise IOError("Unable to connect to Orbital API")
