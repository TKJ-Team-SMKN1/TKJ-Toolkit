import pytest

from IPv4.ip_addr import validate_ip


def test_valid_ip():
    assert validate_ip("192.168.1.10") == "192.168.1.10"


def test_valid_ip_with_spaces():
    assert validate_ip(" 192.168.1.10 ") == "192.168.1.10"


def test_invalid_ip():
    with pytest.raises(ValueError):
        validate_ip("999.999.999.999")


def test_invalid_text():
    with pytest.raises(ValueError):
        validate_ip("hello")


def test_invalid_ipv6():
    with pytest.raises(ValueError):
        validate_ip("2001:db8::1")