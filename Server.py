import socket
import sys


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received ", len(data), "bytes from ", addr)
    print("adresa", addr)

    if data:
        print("aici trimit!")
        sent = sock.sendto(data, addr)

    print("data de la client", data)

   # print("PRESS CTRL-C TO EXIT THE PROG...")
    #try:
     #   while True:
     #       pass
    #except KeyboardInterrupt:
    #    print ("Exiting")
     #   exit(0)




