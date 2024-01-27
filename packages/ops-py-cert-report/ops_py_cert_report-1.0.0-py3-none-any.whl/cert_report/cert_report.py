#!/usr/bin/env python

import ssl
import socket
import logging
from datetime import datetime

########################################################################################################################


def set_timestamp(fmt, s):
    """Returns a date object of a string in the provided format (fmt).

    The string has to be in the correct format, if not None is returned."""

    try:
        ts = datetime.strptime(str(s.strip()), fmt)
    except ValueError:
        logging.error(f"Unable to convert provided argument '{str(s)}' to timestamp object")
        return

    return ts


class CertReport(object):
    def __init__(self, hostnames, warning, critical, skip_ok=False):
        self.hostnames = hostnames
        self.warning = warning
        self.critical = critical
        self.skip_ok = skip_ok
        self.ok_symbol = ":white_check_mark:"
        self.warning_symbol = ":warning:"
        self.critical_symbol = ":bangbang:"
        self.expired_symbol = ":rotating_light:"
        self.endpoint = "/v2/customers/my/invoices"
        self.date_format = "%b %d %H:%M:%S %Y"
        self.now = datetime.now()
        self.report = []
        self.certs = []

    def parse_certs(self):
        for c in self.hostnames:
            self.ssl_cert_expire(c)

    def ssl_cert_expire(self, crt):
        context = ssl.create_default_context()

        with socket.create_connection((crt, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=crt) as s:
                s.do_handshake()
                cert = s.getpeercert()
                not_after = cert.get("notAfter")
                ts = set_timestamp(self.date_format, not_after.rstrip("GMT"))
                age = (self.now - ts).days

                c = {"name": crt,
                     "notAfter": not_after,
                     "expire_ts": ts,
                     "expire_age": age
                     }
                self.certs.append(c)

    def gen_report(self):
        for c in self.certs:
            name = c.get("name")
            expire_date = c.get("notAfter")
            days = c.get("expire_age")

            if days < 0:
                row = f"{name} will expire in {abs(days)} days ({expire_date})."
                if abs(days) <= self.critical:
                    row = f"{self.critical_symbol} {row}"
                elif self.warning >= abs(days) > self.critical:
                    row = f"{self.warning_symbol} {row}"
                else:
                    row = f"{self.ok_symbol} {row}"
            else:
                row = f"{name} has already expired. Expired {abs(days)} days ago ({expire_date})."
                if abs(days) <= self.critical:
                    row = f"{self.expired_symbol} {row}"

            if row:
                row += "\n"
                self.report.append((days, row))

    def get_report(self):
        for e in sorted(self.report, reverse=True):
            yield e[-1]
