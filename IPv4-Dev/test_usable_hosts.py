import pytest

from IPv4.usable_hosts import get_usable_hosts


def test_usable_hosts_24():
    result = get_usable_hosts("192.168.1.10", "/24")

    assert result["first"] == "192.168.1.1"
    assert result["last"] == "192.168.1.254"
    assert result["usable"] == 254


def test_usable_hosts_30():
    result = get_usable_hosts("192.168.1.10", "/30")

    assert result["first"] == "192.168.1.9"
    assert result["last"] == "192.168.1.10"
    assert result["usable"] == 2


def test_usable_hosts_31():
    result = get_usable_hosts("192.168.1.10", "/31")

    assert result["first"] == "192.168.1.10"
    assert result["last"] == "192.168.1.11"
    assert result["usable"] == 2


def test_usable_hosts_32():
    result = get_usable_hosts("192.168.1.10", "/32")

    assert result["first"] == "192.168.1.10"
    assert result["last"] == "192.168.1.10"
    assert result["usable"] == 1


def test_usable_hosts_16():
    result = get_usable_hosts("172.16.10.20", "/16")

    assert result["first"] == "172.16.0.1"
    assert result["last"] == "172.16.255.254"
    assert result["usable"] == 65534


def test_invalid_ip():
    with pytest.raises(ValueError):
        get_usable_hosts("999.999.999.999", "/24")


def test_invalid_cidr():
    with pytest.raises(ValueError):
        get_usable_hosts("192.168.1.10", "/33")