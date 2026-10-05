def validate_cidr(cidr: str) -> int:
    """
    Validate an IPv4 CIDR prefix.

    Accepts:
        24
        /24
        "24"
        "/24"

    Returns:
        int: CIDR prefix from 0 to 32.

    Raises:
        ValueError: If the CIDR is invalid.
    """
    value = str(cidr).strip()

    if value.startswith("/"):
        value = value[1:]

    if "/" in value:
        raise ValueError("Invalid CIDR format")

    if not value.isdigit():
        raise ValueError("CIDR must be a number from 0 to 32")

    prefix = int(value)

    if not 0 <= prefix <= 32:
        raise ValueError("CIDR must be between 0 and 32")

    return prefix