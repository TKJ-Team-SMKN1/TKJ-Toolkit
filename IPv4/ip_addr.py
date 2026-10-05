import ipaddress


def validate_ip(ip: str) -> str:
    """
    Validate an IPv4 address.

    Returns:
        str: Normalized IPv4 address.

    Raises:
        ValueError: If the IP address is invalid.
    """
    try:
        address = ipaddress.IPv4Address(ip.strip())
        return str(address)
    except ipaddress.AddressValueError as exc:
        raise ValueError("Invalid IPv4 address") from exc