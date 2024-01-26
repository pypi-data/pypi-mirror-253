#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This module implements WHOIS protocol and performs WHOIS requests.
#    Copyright (C) 2024  SimpleWhois

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This module implements WHOIS protocol and performs WHOIS requests.
"""

__version__ = "0.0.4"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This module implements WHOIS protocol and performs WHOIS requests.
"""
__url__ = "https://github.com/mauricelambert/SimpleWhois"

__all__ = ["whois", "whois_ipv6", "whois_ipv4", "whois_domain"]

__license__ = "GPL-3.0 License"
__copyright__ = """
SimpleWhois  Copyright (C) 2024  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
copyright = __copyright__
license = __license__

print(copyright)

# from json import load
from socket import socket

# from contextlib import suppress
from urllib.parse import urlparse

# from urllib.request import urlopen
from sys import argv, stderr, exit, executable
from ipaddress import ip_address, IPv4Address, IPv6Address, ip_network

databasev4 = {
    "description": "RDAP bootstrap file for IPv4 address allocations",
    "publication": "2019-06-07T19:00:02Z",
    "services": [
        [
            [
                "41.0.0.0/8",
                "102.0.0.0/8",
                "105.0.0.0/8",
                "154.0.0.0/8",
                "196.0.0.0/8",
                "197.0.0.0/8",
            ],
            [
                "https://rdap.afrinic.net/rdap/",
                "http://rdap.afrinic.net/rdap/",
            ],
        ],
        [
            [
                "1.0.0.0/8",
                "14.0.0.0/8",
                "27.0.0.0/8",
                "36.0.0.0/8",
                "39.0.0.0/8",
                "42.0.0.0/8",
                "43.0.0.0/8",
                "49.0.0.0/8",
                "58.0.0.0/8",
                "59.0.0.0/8",
                "60.0.0.0/8",
                "61.0.0.0/8",
                "101.0.0.0/8",
                "103.0.0.0/8",
                "106.0.0.0/8",
                "110.0.0.0/8",
                "111.0.0.0/8",
                "112.0.0.0/8",
                "113.0.0.0/8",
                "114.0.0.0/8",
                "115.0.0.0/8",
                "116.0.0.0/8",
                "117.0.0.0/8",
                "118.0.0.0/8",
                "119.0.0.0/8",
                "120.0.0.0/8",
                "121.0.0.0/8",
                "122.0.0.0/8",
                "123.0.0.0/8",
                "124.0.0.0/8",
                "125.0.0.0/8",
                "126.0.0.0/8",
                "133.0.0.0/8",
                "150.0.0.0/8",
                "153.0.0.0/8",
                "163.0.0.0/8",
                "171.0.0.0/8",
                "175.0.0.0/8",
                "180.0.0.0/8",
                "182.0.0.0/8",
                "183.0.0.0/8",
                "202.0.0.0/8",
                "203.0.0.0/8",
                "210.0.0.0/8",
                "211.0.0.0/8",
                "218.0.0.0/8",
                "219.0.0.0/8",
                "220.0.0.0/8",
                "221.0.0.0/8",
                "222.0.0.0/8",
                "223.0.0.0/8",
            ],
            ["https://rdap.apnic.net/"],
        ],
        [
            [
                "3.0.0.0/8",
                "4.0.0.0/8",
                "6.0.0.0/8",
                "7.0.0.0/8",
                "8.0.0.0/8",
                "9.0.0.0/8",
                "11.0.0.0/8",
                "12.0.0.0/8",
                "13.0.0.0/8",
                "15.0.0.0/8",
                "16.0.0.0/8",
                "17.0.0.0/8",
                "18.0.0.0/8",
                "19.0.0.0/8",
                "20.0.0.0/8",
                "21.0.0.0/8",
                "22.0.0.0/8",
                "23.0.0.0/8",
                "24.0.0.0/8",
                "26.0.0.0/8",
                "28.0.0.0/8",
                "29.0.0.0/8",
                "30.0.0.0/8",
                "32.0.0.0/8",
                "33.0.0.0/8",
                "34.0.0.0/8",
                "35.0.0.0/8",
                "38.0.0.0/8",
                "40.0.0.0/8",
                "44.0.0.0/8",
                "45.0.0.0/8",
                "47.0.0.0/8",
                "48.0.0.0/8",
                "50.0.0.0/8",
                "52.0.0.0/8",
                "54.0.0.0/8",
                "55.0.0.0/8",
                "56.0.0.0/8",
                "63.0.0.0/8",
                "64.0.0.0/8",
                "65.0.0.0/8",
                "66.0.0.0/8",
                "67.0.0.0/8",
                "68.0.0.0/8",
                "69.0.0.0/8",
                "70.0.0.0/8",
                "71.0.0.0/8",
                "72.0.0.0/8",
                "73.0.0.0/8",
                "74.0.0.0/8",
                "75.0.0.0/8",
                "76.0.0.0/8",
                "96.0.0.0/8",
                "97.0.0.0/8",
                "98.0.0.0/8",
                "99.0.0.0/8",
                "100.0.0.0/8",
                "104.0.0.0/8",
                "107.0.0.0/8",
                "108.0.0.0/8",
                "128.0.0.0/8",
                "129.0.0.0/8",
                "130.0.0.0/8",
                "131.0.0.0/8",
                "132.0.0.0/8",
                "134.0.0.0/8",
                "135.0.0.0/8",
                "136.0.0.0/8",
                "137.0.0.0/8",
                "138.0.0.0/8",
                "139.0.0.0/8",
                "140.0.0.0/8",
                "142.0.0.0/8",
                "143.0.0.0/8",
                "144.0.0.0/8",
                "146.0.0.0/8",
                "147.0.0.0/8",
                "148.0.0.0/8",
                "149.0.0.0/8",
                "152.0.0.0/8",
                "155.0.0.0/8",
                "156.0.0.0/8",
                "157.0.0.0/8",
                "158.0.0.0/8",
                "159.0.0.0/8",
                "160.0.0.0/8",
                "161.0.0.0/8",
                "162.0.0.0/8",
                "164.0.0.0/8",
                "165.0.0.0/8",
                "166.0.0.0/8",
                "167.0.0.0/8",
                "168.0.0.0/8",
                "169.0.0.0/8",
                "170.0.0.0/8",
                "172.0.0.0/8",
                "173.0.0.0/8",
                "174.0.0.0/8",
                "184.0.0.0/8",
                "192.0.0.0/8",
                "198.0.0.0/8",
                "199.0.0.0/8",
                "204.0.0.0/8",
                "205.0.0.0/8",
                "206.0.0.0/8",
                "207.0.0.0/8",
                "208.0.0.0/8",
                "209.0.0.0/8",
                "214.0.0.0/8",
                "215.0.0.0/8",
                "216.0.0.0/8",
            ],
            [
                "https://rdap.arin.net/registry/",
                "http://rdap.arin.net/registry/",
            ],
        ],
        [
            [
                "2.0.0.0/8",
                "5.0.0.0/8",
                "25.0.0.0/8",
                "31.0.0.0/8",
                "37.0.0.0/8",
                "46.0.0.0/8",
                "51.0.0.0/8",
                "53.0.0.0/8",
                "57.0.0.0/8",
                "62.0.0.0/8",
                "77.0.0.0/8",
                "78.0.0.0/8",
                "79.0.0.0/8",
                "80.0.0.0/8",
                "81.0.0.0/8",
                "82.0.0.0/8",
                "83.0.0.0/8",
                "84.0.0.0/8",
                "85.0.0.0/8",
                "86.0.0.0/8",
                "87.0.0.0/8",
                "88.0.0.0/8",
                "89.0.0.0/8",
                "90.0.0.0/8",
                "91.0.0.0/8",
                "92.0.0.0/8",
                "93.0.0.0/8",
                "94.0.0.0/8",
                "95.0.0.0/8",
                "109.0.0.0/8",
                "141.0.0.0/8",
                "145.0.0.0/8",
                "151.0.0.0/8",
                "176.0.0.0/8",
                "178.0.0.0/8",
                "185.0.0.0/8",
                "188.0.0.0/8",
                "193.0.0.0/8",
                "194.0.0.0/8",
                "195.0.0.0/8",
                "212.0.0.0/8",
                "213.0.0.0/8",
                "217.0.0.0/8",
            ],
            ["https://rdap.db.ripe.net/"],
        ],
        [
            [
                "177.0.0.0/8",
                "179.0.0.0/8",
                "181.0.0.0/8",
                "186.0.0.0/8",
                "187.0.0.0/8",
                "189.0.0.0/8",
                "190.0.0.0/8",
                "191.0.0.0/8",
                "200.0.0.0/8",
                "201.0.0.0/8",
            ],
            ["https://rdap.lacnic.net/rdap/"],
        ],
    ],
    "version": "1.0",
}

databasev6 = {
    "description": "RDAP bootstrap file for IPv6 address allocations",
    "publication": "2019-11-06T19:00:04Z",
    "services": [
        [
            ["2001:4200::/23", "2c00::/12"],
            [
                "https://rdap.afrinic.net/rdap/",
                "http://rdap.afrinic.net/rdap/",
            ],
        ],
        [
            [
                "2001:200::/23",
                "2001:4400::/23",
                "2001:8000::/19",
                "2001:a000::/20",
                "2001:b000::/20",
                "2001:c00::/23",
                "2001:e00::/23",
                "2400::/12",
            ],
            ["https://rdap.apnic.net/"],
        ],
        [
            [
                "2001:1800::/23",
                "2001:400::/23",
                "2001:4800::/23",
                "2600::/12",
                "2610::/23",
                "2620::/23",
                "2630::/12",
            ],
            [
                "https://rdap.arin.net/registry/",
                "http://rdap.arin.net/registry/",
            ],
        ],
        [
            [
                "2001:1400::/22",
                "2001:1a00::/23",
                "2001:1c00::/22",
                "2001:2000::/19",
                "2001:4000::/23",
                "2001:4600::/23",
                "2001:4a00::/23",
                "2001:4c00::/23",
                "2001:5000::/20",
                "2001:600::/23",
                "2001:800::/22",
                "2003::/18",
                "2a00::/12",
                "2a10::/12",
            ],
            ["https://rdap.db.ripe.net/"],
        ],
        [["2001:1200::/23", "2800::/12"], ["https://rdap.lacnic.net/rdap/"]],
    ],
    "version": "1.0",
}

ip_requests_arguments = {
    "whois.arin.net": "n + ",
    "whois.ripe.net": "-V Md5.5.20 ",
    "whois.lacnic.net": "",
    "whois.apnic.net": "-V Md5.5.20 ",
    "whois.afrinic.net": "-V Md5.5.20 ",
}

# with suppress(Exception):
#     databasev4 = load(urlopen("https://data.iana.org/rdap/ipv4.json"))

# with suppress(Exception):
#     databasev6 = load(urlopen("https://data.iana.org/rdap/ipv6.json"))


def whois(target: str) -> str:
    """
    This function checks target type and call the whois_[type] function.
    """

    try:
        ip = ip_address(target)
    except ValueError:
        return whois_domain(target)
    else:
        if isinstance(ip, IPv4Address):
            return whois_ipv4(target)
        elif isinstance(ip, IPv6Address):
            return whois_ipv6(target)

    return whois_domain(target)


def whois_domain(domain: str, server: str = None) -> str:
    """
    This function performs WHOIS requests for a domain.
    """

    domain = domain.lower()

    s = socket()
    s.connect(
        (
            server or "whois.iana.org"
            if not (
                domain.endswith(".com")
                or domain.endswith(".net")
                or domain.endswith(".edu")
            )
            else "whois.verisign-grs.com",
            43,
        )
    )
    s.sendall(domain.encode() + b"\r\n")

    data = bytearray()
    new_data = True

    while new_data:
        new_data = s.recv(65535)
        data.extend(new_data)

    s.close()

    if server is not None:
        return data.decode("latin-1")

    data2 = ""
    for line in data.splitlines():
        if line.strip().startswith(
            b"Registrar WHOIS Server:"
        ) or line.strip().startswith(b"whois:"):
            data2 = whois_domain(
                domain, line.split(b":", 1)[1].strip().decode()
            )

    return data.decode("latin-1") + data2


def get_rir_hostname(ip: str, database: dict) -> str:
    """
    This function returns the RIR hostname for the IP address.
    """

    ip_object = ip_address(ip)
    for db in database["services"]:
        for ip_range in db[0]:
            if ip_object in ip_network(ip_range):
                return "whois." + ".".join(
                    urlparse(db[1][0]).hostname.split(".")[-2:]
                )


def whois_ipv6(ip: str) -> str:
    """
    This function performs WHOIS requests for a IPv6.
    """

    s = socket()
    server = get_rir_hostname(ip, databasev6)
    s.connect((server, 43))
    s.sendall(ip_requests_arguments[server].encode() + ip.encode() + b"\r\n")

    data = bytearray()
    new_data = True

    while new_data:
        new_data = s.recv(65535)
        data.extend(new_data)

    s.close()
    return data.decode("latin-1")


def whois_ipv4(ip: str) -> str:
    """
    This function performs WHOIS requests for a IPv4.
    """

    s = socket()
    server = get_rir_hostname(ip, databasev4)
    s.connect((server, 43))
    s.sendall(ip_requests_arguments[server].encode() + ip.encode() + b"\r\n")

    data = bytearray()
    new_data = True

    while new_data:
        new_data = s.recv(65535)
        data.extend(new_data)

    s.close()
    return data.decode("latin-1")


if __name__ == "__main__":
    exit_code = 0
    if len(argv) < 2:
        print(
            f'USAGES: "{executable}" "{argv[0]}" '
            "ip_or_domain1 [ip_or_domain2] ... [ip_or_domainX]",
            file=stderr,
        )
        exit_code = 1

    for domain in argv[1:]:
        print(whois(domain))
    exit(exit_code)
