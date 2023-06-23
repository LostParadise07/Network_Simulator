import socket

class ApplicationLayer:
    def __init__(self, device):
        self.device = device

    def send(self, destination, data):
        # Simulate application layer protocol (e.g., HTTP, FTP, SMTP)
        # Here, we are using a simple echo protocol

        try:
            # Create a socket for communication
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the destination device using its IP address and port
            destination_ip = destination.getIPAddress()
            destination_port = destination.getPort()
            sock.connect((destination_ip, destination_port))

            # Send data to the destination device
            sock.sendall(data.encode())

            # Receive the response from the destination device
            response = sock.recv(1024).decode()

            # Print the response
            print(f"Received response from {destination.getName()}: {response}")

        except ConnectionRefusedError:
            print(f"Connection refused: Unable to connect to {destination.getName()}")

        except Exception as e:
            print(f"An error occurred while sending data to {destination.getName()}: {str(e)}")

        finally:
            # Close the socket
            sock.close()
