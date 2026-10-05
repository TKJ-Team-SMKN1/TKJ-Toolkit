import pytest

from IPv4.broadcast import get_broadcast


def test_broadcast_24():
    assert get_broadcast("192.168.1.10", "/24") == "192.168.1.255"


def test_broadcast_16():
    assert get_broadcast("172.16.10.20", "/16") == "172.16.255.255"


def test_broadcast_8():
    assert get_broadcast("10.20.30.40", "/8") == "10.255.255.255"


def test_broadcast_30():
    assert get_broadcast("192.168.1.10", "/30") == "192.168.1.11"


def test_broadcast_already_network():
    assert get_broadcast("192.168.1.0", "/24") == "192.168.1.255"


def test_invalid_ip():
    with pytest.raises(ValueError):
        get_broadcast("999.999.999.999", "/24")


def test_invalid_cidr():
    with pytest.raises(ValueError):
        get_broadcast("192.168.1.10", "/33")