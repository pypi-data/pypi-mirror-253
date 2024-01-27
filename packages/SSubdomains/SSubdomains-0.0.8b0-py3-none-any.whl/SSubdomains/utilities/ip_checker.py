import ipaddress


def is_ip_in_range(ip_to_check, range_from, range_to):
    ip_from = ipaddress.IPv4Address(range_from)
    ip_to = ipaddress.IPv4Address(range_to)
    ip_to_check = ipaddress.IPv4Address(ip_to_check)
    return ip_from <= ip_to_check <= ip_to
