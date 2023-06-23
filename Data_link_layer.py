from Hub import *
from Switch import *
import time
from Broadcast import *

def Data_link_layer(data3,sourceDevice):
        c3 = int(input("What's your Choice?\n1: HubSwitchHub-Configuration 2: SwitchDevice-Configuration\n"))
        if c3 == 1:
            print()
            print("*******************************************************")
            print("HubSwitchHub-Configuration")

            # Create end devices and hubs
            A = Device("A")
            B = Device("B")
            C = Device("C")
            D = Device("D")
            E = Device("E")
            hub1 = Hub("hub1")
            hub2 = Hub("hub2")

            # Connect devices to hubs
            hub1.connect(A)
            hub1.connect(B)
            hub1.connect(C)
            hub2.connect(D)
            hub2.connect(E)

            # Set data for source device
            if sourceDevice not in ["A", "B", "C", "D", "E"]:
                print("Invalid SourceDevice")
                return
            if sourceDevice == "A":
                A.setData(data3)
            elif sourceDevice == "B":
                B.setData(data3)
            elif sourceDevice == "C":
                C.setData(data3)
            elif sourceDevice == "D":
                D.setData(data3)
            elif sourceDevice == "E":
                E.setData(data3)

            # Print devices' data before transmission
            print()
            print("*******************************************************")
            print("DevicesData before Transmission:")
            print("A data before Transmission:", A.data)
            print("B data before Transmission:", B.data)
            print("C data before Transmission:", C.data)
            print("D data before Transmission:", D.data)
            print("E data before Transmission:", E.data)

            # Perform broadcast transmission
            connected_devices = hub1.getConnectedDevices() + hub2.getConnectedDevices()
            broadcast_function(sourceDevice, data3, connected_devices)
            print()
            print("*******************************************************")

            # Determine which hub is transferring the data and which hub is sending the data
            transfer_hub = hub1 if sourceDevice in ["A", "B", "C"] else hub2
            sending_hub = hub1 if transfer_hub == hub2 else hub2

            # Calculate the broadcast domain
            broadcast_domain = len(connected_devices)

            # Calculate the collision domain
            collision_domain = len(hub1.getConnectedDevices()) + len(hub2.getConnectedDevices())

            # Print transfer and sending hub information
            print("Transfer Hub:", transfer_hub.name)
            print("Sending Hub:", sending_hub.name)

            # Print devices' data after transmission
            print("DevicesData after Transmission:")
            print("A data after Transmission:", A.data)
            print("B data after Transmission:", B.data)
            print("C data after Transmission:", C.data)
            print("D data after Transmission:", D.data)
            print("E data after Transmission:", E.data)

            # Calculate and print total time taken for transmission
            time_taken = time.process_time()
            print()
            print("*******************************************************")
            print("Total Time Taken for Transmission:", time_taken)
            print("Broadcast domain =", broadcast_domain, "and Collision domain =", collision_domain)

        elif c3 == 2:
            print("SwitchDevice-Configuration")
            TotDevices = int(input("Give total number of end devices:\n"))
            bridge_count = 0

            SourceDevice2 = int(input("Choose source from 1, 2, 3:\n"))
            print()
            print("*******************************************************")
            destinationDevice2 = int(input("Choose Destination from 1, 2, 3 (shouldn't be the same as Source):\n"))
            print()
            print("*******************************************************")
            print("Data to be transmitted will be", data3, ":\n")
            print()
            print("*******************************************************")
            bridge_count += 1

            if bridge_count == 1:
                # Create switch
                switch = Switch()

                # Create devices and connect them to the switch
                devices = [Device(f"Device {i+1}") for i in range(TotDevices)]

                for i in range(TotDevices):
                    switch.connect(devices[i])

                # Set data for the source device
                sourceDevice2 = devices[SourceDevice2 - 1]
                sourceDevice2.setData(data3)

                start = time.process_time()

                for j in range(TotDevices):
                    if j == SourceDevice2 - 1:
                        continue
                    for i in range(len(data3)):
                        devices[destinationDevice2 - 1].data += data3[i]
                        if j == destinationDevice2 - 1:
                            print("Received frame number:", i + 1, "at The Destination", j + 1)
                            print("Received frame number:", i + 1)
                            print("The source", SourceDevice2, "received the ACK")
                        else:
                            break
                        
                time_taken = time.process_time() - start
                print()
                print("*******************************************************")
                print("Total Time Taken for Transmission:", time_taken)

                # Calculate the broadcast domain
                broadcast_domain = 1

                # Calculate the collision domain
                collision_domain = TotDevices

                print("Broadcast domain =", broadcast_domain, "and Collision domain =", collision_domain)

            else:
                print("Invalid Choice")
                return
            
    