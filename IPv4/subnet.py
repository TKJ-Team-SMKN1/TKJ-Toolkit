import ipaddress

from .ip_addr import validate_ip
from .cidr import validate_cidr


def get_subnet(ip: str, cidr: str) -> str:
    """
    Calculate the subnet mask from IPv4 + CIDR.

    Example:
        192.168.1.10 + /24
        -> 255.255.255.0
    """
    ip = validate_ip(ip)
    prefix = validate_cidr(cidr)

    network = ipaddress.IPv4Network(
        f"{ip}/{prefix}",
        strict=False
    )

    return str(network.netmask)