import pytest

from IPv4.total_addr import get_total_addresses


def test_total_addresses_24():
    assert get_total_addresses("192.168.1.10", "/24") == 256


def test_total_addresses_16():
    assert get_total_addresses("172.16.10.20", "/16") == 65536


def test_total_addresses_8():
    assert get_total_addresses("10.20.30.40", "/8") == 16777216


def test_total_addresses_30():
    assert get_total_addresses("192.168.1.10", "/30") == 4


def test_total_addresses_31():
    assert get_total_addresses("192.168.1.10", "/31") == 2


def test_total_addresses_32():
    assert get_total_addresses("192.168.1.10", "/32") == 1


def test_total_addresses_without_slash():
    assert get_total_addresses("192.168.1.10", "24") == 256


def test_invalid_ip():
    with pytest.raises(ValueError):
        get_total_addresses("999.999.999.999", "/24")


def test_invalid_cidr():
    with pytest.raises(ValueError):
        get_total_addresses("192.168.1.10", "/33")