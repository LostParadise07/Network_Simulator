# TransportLayer.py

class TransportLayer:
    def __init__(self):
        self.portTable = {}

    def openPort(self, device, port):
        self.portTable[device] = port

    def getPort(self, device):
        return self.portTable.get(device, None)


class TCP:
    def __init__(self, transport_layer):
        self.transportLayer = transport_layer

    def establishConnection(self, source_device, destination_device):
        source_port = self.transportLayer.getPort(source_device)
        destination_port = self.transportLayer.getPort(destination_device)

        if source_port is None or destination_port is None:
            print("Source or destination device does not have an assigned port.")
            return

        print(f"Establishing TCP connection from {source_device.name}:{source_port} "
              f"to {destination_device.name}:{destination_port}")

    def closeConnection(self, source_device, destination_device):
        source_port = self.transportLayer.getPort(source_device)
        destination_port = self.transportLayer.getPort(destination_device)

        if source_port is None or destination_port is None:
            print("Source or destination device does not have an assigned port.")
            return

        print(f"Closing TCP connection from {source_device.name}:{source_port} "
              f"to {destination_device.name}:{destination_port}")

