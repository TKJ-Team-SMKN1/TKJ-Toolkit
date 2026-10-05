import pytest

from IPv4.network_addr import get_network_address


def test_network_address_24():
    assert get_network_address("192.168.1.10", "/24") == "192.168.1.0"


def test_network_address_16():
    assert get_network_address("172.16.10.20", "/16") == "172.16.0.0"


def test_network_address_8():
    assert get_network_address("10.20.30.40", "/8") == "10.0.0.0"


def test_network_address_30():
    assert get_network_address("192.168.1.10", "/30") == "192.168.1.8"


def test_network_address_already_network():
    assert get_network_address("192.168.1.0", "/24") == "192.168.1.0"


def test_invalid_ip():
    with pytest.raises(ValueError):
        get_network_address("999.999.999.999", "/24")


def test_invalid_cidr():
    with pytest.raises(ValueError):
        get_network_address("192.168.1.10", "/33")