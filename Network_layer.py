# NetworkLayer.py
class NetworkLayer:
    def __init__(self):
        self.ipAddressTable = {}

    def assignIPAddress(self, device, ip_address):
        self.ipAddressTable[device] = ip_address

    def getIPAddress(self, device):
        return self.ipAddressTable.get(device, None)


class DHCP:
    def __init__(self, network_layer):
        self.networkLayer = network_layer
        self.availableIPs = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4", "192.168.0.5"]

    def requestIP(self, device):
        if device in self.networkLayer.ipAddressTable:
            return

        if len(self.availableIPs) > 0:
            ip_address = self.availableIPs.pop(0)
            self.networkLayer.assignIPAddress(device, ip_address)
            print(f"Assigned IP address {ip_address} to {device.name}")
        else:
            print(f"No available IP addresses for {device.name}")

