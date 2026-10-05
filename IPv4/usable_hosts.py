import ipaddress

from .ip_addr import validate_ip
from .cidr import validate_cidr


def get_usable_hosts(ip: str, cidr: str) -> dict:
    """
    Calculate the first and last usable host.

    Rules:
        /0 - /30 -> network/broadcast excluded
        /31      -> both addresses usable
        /32      -> single address
    """
    ip = validate_ip(ip)
    prefix = validate_cidr(cidr)

    network = ipaddress.IPv4Network(
        f"{ip}/{prefix}",
        strict=False
    )

    total = network.num_addresses

    if prefix <= 30:
        first = network.network_address + 1
        last = network.broadcast_address - 1
        usable = max(total - 2, 0)

    elif prefix == 31:
        first = network.network_address
        last = network.broadcast_address
        usable = 2

    else:  # /32
        first = network.network_address
        last = network.network_address
        usable = 1

    return {
        "first": str(first),
        "last": str(last),
        "usable": usable,
    }