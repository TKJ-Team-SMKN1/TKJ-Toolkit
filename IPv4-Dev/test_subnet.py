import pytest

from IPv4.subnet import get_subnet


def test_subnet_24():
    assert get_subnet("192.168.1.10", "/24") == "255.255.255.0"


def test_subnet_16():
    assert get_subnet("172.16.10.20", "/16") == "255.255.0.0"


def test_subnet_8():
    assert get_subnet("10.20.30.40", "/8") == "255.0.0.0"


def test_subnet_30():
    assert get_subnet("192.168.1.10", "/30") == "255.255.255.252"


def test_subnet_without_slash():
    assert get_subnet("192.168.1.10", "24") == "255.255.255.0"


def test_invalid_ip():
    with pytest.raises(ValueError):
        get_subnet("999.999.999.999", "/24")


def test_invalid_cidr():
    with pytest.raises(ValueError):
        get_subnet("192.168.1.10", "/33")