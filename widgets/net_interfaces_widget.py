# encoding: utf-8
import npyscreen
import netifaces


class NetInterfacesWidget(npyscreen.BoxTitle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.editable = False

    @staticmethod
    def ip_addresses():
        PROTO = netifaces.AF_INET  # We want only IPv4, for now at least
        # Get list of network interfaces
        ifaces = netifaces.interfaces()

        # Get addresses for each interface
        if_addrs = [(netifaces.ifaddresses(iface), iface) for iface in ifaces]

        # Filter
        if_inet_addrs = [(tup[0][PROTO], tup[1]) for tup in if_addrs if
                         PROTO in tup[0] and _is_external_interface(tup[1])]

        return ["{}: {}".format(tup[1], s['addr']) for tup in if_inet_addrs for s in tup[0] if 'addr' in s]

    def update(self, *args, **kwargs):
        self.values = self.ip_addresses()
        super().update(*args, **kwargs)


def _is_external_interface(interface_name):
    IGNORE_INTERFACE_PREFIXES = ('lo', 'docker', 'br')
    for interface in IGNORE_INTERFACE_PREFIXES:
        if interface_name.startswith(interface):
            return False
    return True
