"""
Some helper functions to get adapter names and ipv4 subnets on that adapter
"""
import ipaddress

import ifaddr


def compressed_subnet(host, bits):
    """
    Given an ip and number of bits, (e.g. 10.0.3.1, 8), returns the compressed
    subnet mask (10.0.0.0/8)
    """
    net_string = '{host}/{bits}'.format(host=host, bits=bits)
    network = ipaddress.ip_network(net_string, strict=False)
    return network.compressed


def get_subnets(adapter_name='wlan0'):
    """
    Returns a list of ipv4 subnet strings for the given adapter.
    """
    all_adapters = {adapter.name: adapter
                    for adapter in ifaddr.get_adapters()}
    adapter = all_adapters[adapter_name]

    subnets = {compressed_subnet(ip.ip, ip.network_prefix)
               for ip in adapter.ips
               if len(ip.ip) > 3}

    return list(subnets)


def get_adapter_names():
    """
    Returns a list of available adapter names
    """
    return [adapter.name for adapter in ifaddr.get_adapters()]
