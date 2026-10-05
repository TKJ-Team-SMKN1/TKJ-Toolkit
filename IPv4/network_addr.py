import ipaddress

from .ip_addr import validate_ip
from .cidr import validate_cidr


def get_network_address(ip: str, cidr: str) -> str:
    """
    Calculate the network address.
    """
    ip = validate_ip(ip)
    prefix = validate_cidr(cidr)

    network = ipaddress.IPv4Network(
        f"{ip}/{prefix}",
        strict=False
    )

    return str(network.network_address)