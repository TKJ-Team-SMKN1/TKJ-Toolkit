import pytest

from IPv4.cidr import validate_cidr


def test_valid_cidr_without_slash():
    assert validate_cidr("24") == 24


def test_valid_cidr_with_slash():
    assert validate_cidr("/24") == 24


def test_cidr_zero():
    assert validate_cidr("0") == 0


def test_cidr_32():
    assert validate_cidr("32") == 32


def test_cidr_with_spaces():
    assert validate_cidr(" /24 ") == 24


def test_cidr_with_spaces_without_slash():
    assert validate_cidr(" 24 ") == 24


def test_invalid_cidr_above_32():
    with pytest.raises(ValueError):
        validate_cidr("33")


def test_invalid_cidr_negative():
    with pytest.raises(ValueError):
        validate_cidr("-1")


def test_invalid_cidr_text():
    with pytest.raises(ValueError):
        validate_cidr("abc")


def test_invalid_cidr_multiple_slashes():
    with pytest.raises(ValueError):
        validate_cidr("//24")


def test_invalid_cidr_trailing_slash():
    with pytest.raises(ValueError):
        validate_cidr("24/")


def test_invalid_cidr_mixed_format():
    with pytest.raises(ValueError):
        validate_cidr("/2/4")


def validate_cidr(cidr: str) -> int:
    """
    Validate an IPv4 CIDR prefix.

    Accepts:
        24
        /24

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