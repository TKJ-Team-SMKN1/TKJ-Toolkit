import ipaddress

from .ip_addr import validate_ip
from .cidr import validate_cidr


def get_total_addresses(ip: str, cidr: str) -> int:
    """
    Calculate the total number of IPv4 addresses.
    """
    ip = validate_ip(ip)
    prefix = validate_cidr(cidr)

    network = ipaddress.IPv4Network(
        f"{ip}/{prefix}",
        strict=False
    )

    return network.num_addresses