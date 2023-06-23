from Hub import *
from CRC import *
from Physical_Layer import physicalLayer
from Data_link_layer import Data_link_layer
from Network_layer import *
from Transport_layer import *
from Application_layer import *
def main():
    count="1"
    while(count):
        SD_Data,SourceDevice=physicalLayer()
        print()
        print()
        print("*******************************************************")
        print("Entering into Data Link Layer part\n")
        SD_Data=Data_link_layer(SD_Data,SourceDevice)

        print("*******************************************************")
        print("Entering into Network Layer part\n")
        networkLayer = NetworkLayer()

        # Create an instance of the DHCP class and pass the networkLayer instance
        dhcp = DHCP(networkLayer)

        # Assign IP addresses to devices using DHCP
        dhcp.requestIP(A)
        dhcp.requestIP(B)
        dhcp.requestIP(C)
        dhcp.requestIP(D)
        dhcp.requestIP(E)

        # Retrieve IP addresses from the network layer
        ip_address_A = networkLayer.getIPAddress(A)
        ip_address_B = networkLayer.getIPAddress(B)
        ip_address_C = networkLayer.getIPAddress(C)
        ip_address_D = networkLayer.getIPAddress(D)
        ip_address_E = networkLayer.getIPAddress(E)

        print("*******************************************************")
        print("Printing IP Address Table\n")
        
        print("IP Address for Device A:", ip_address_A)
        print("IP Address for Device B:", ip_address_B)
        print("IP Address for Device C:", ip_address_C)
        print("IP Address for Device D:", ip_address_D)
        print("IP Address for Device E:", ip_address_E)

        print("*******************************************************")
        print("Entering into Transport Layer part\n")
        
        transportLayer = TransportLayer()

        # Assign ports to devices
        transportLayer.openPort(A, 8000)
        transportLayer.openPort(B, 9000)
        transportLayer.openPort(C, 7000)
        transportLayer.openPort(D, 6000)
        transportLayer.openPort(E, 5000)

        # Create an instance of the TCP class and pass the transportLayer instance
        tcp = TCP(transportLayer)

        # Establish TCP connections
        tcp.establishConnection(A, B)
        tcp.establishConnection(C, D)
        tcp.establishConnection(D, E)

        # Close TCP connections
        tcp.closeConnection(A, B)
        tcp.closeConnection(C, D)
        tcp.closeConnection(D, E)

        print("*******************************************************")
        print("Entering into Application Layer part\n")

        application_A = ApplicationLayer(A)
        application_B = ApplicationLayer(B)
        application_C = ApplicationLayer(C)
        application_D = ApplicationLayer(D)
        application_E = ApplicationLayer(E)

        # Devices communicate at the Application Layer
        application_A.send(B, "Hello, B!")
        application_B.send(A, "Hi, A!")
        application_C.send(D, "Greetings, D!")
        application_D.send(C, "Salutations, C!")
        application_E.send(A, "Hey, A!")


        count=input("To Continue Press 1 else exit:")
        if(count!="1"):
            break

if __name__ == "__main__":
    main()
