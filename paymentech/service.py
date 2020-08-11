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
    version = paymentech.configuration.get("version")
    maximum_attempts = paymentech.configuration.get("attempts", 3)
    urls = endpoints[environment]
    trace = str(random.randint(1, 9999999999999999))

    headers = {
        "MIME-Version": "1.1",
        "Content-type": "application/PTI80",
        "Content-transfer-encoding": "text",
        "Request-Number": "1",
        "Document-type": "Request",
        "Trace-Number": trace,
        "Interface-Version": f"Chase Paymentech Python SDK/{version}"
    }

    # If we are forcing failover, skip the first URL
    if paymentech.configuration.get("failover", False):
        urls = urls[1:]

    for url in urls:
        for attempt in range(maximum_attempts):
            try:
                response = requests.post(url, data=payload, headers=headers)

                if response and response.text:
                    return trace, response.text
            except Exception:
                pass

            # Avoid throttling
            time.sleep(0.5)

    raise IOError("Unable to connect to Orbital API")
