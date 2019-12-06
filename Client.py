import socket

class Client_request():
    def __init__(self):
        pass

    def request(self):
        UDP_IP = "127.0.0.1"
        UDP_PORT = 5005
        addr = (UDP_IP, UDP_PORT)

        print("UDP target IP:", UDP_IP)
        print("UDP target port:", UDP_PORT)

        oras = input("introdu numele orasului: ")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        # sock.sendto(MESSAGE.encode("utf-8"), (UDP_IP, UDP_PORT))
        try:
            sock.sendto(oras.encode("utf-8"), addr)
            print("receive response")
            data, addr = sock.recvfrom(1024)
            print("Data primita este", repr(data))
        finally:
            sock.close()
        return oras
