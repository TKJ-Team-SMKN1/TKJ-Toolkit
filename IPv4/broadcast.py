import ipaddress

from .ip_addr import validate_ip
from .cidr import validate_cidr


def get_broadcast(ip: str, cidr: str) -> str:
    """
    Calculate the broadcast address.
    """
    ip = validate_ip(ip)
    prefix = validate_cidr(cidr)

    network = ipaddress.IPv4Network(
        f"{ip}/{prefix}",
        strict=False
    )

    return str(network.broadcast_address)