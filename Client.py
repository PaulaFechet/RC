import socket
from Message_Header import Message_Header
from Parse_Message_Service import Parse_Message_Service
import Defines as d
import logging
import time
import Inputs as input_city
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

addr = (UDP_IP, UDP_PORT)
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

city_list = []
method_list = []
for i in range(1):
    city,method = input_city.inputs()
    city_list.append(city)
    method_list.append(method)
print("city_list:",city_list)
print("methood_list:",method_list)
index_method_list = 0

for i in method_list:
	if i == 1:
		a = d.TYPE_CON
	elif i == 2:
		a = d.TYPE_NON

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
for oras in city_list:
# construim pachetul pe care il trimitem la server
    buildMsg = Message_Header()
    msg = buildMsg.BuildMessage(d.COAP_VERSION, a, d.COAP_CLASS_METHODS,method_list[index_method_list],d.newMessageId(), d.newToken())
    index_method_list +=1
    #buildMsg.Print()
    msg_string = "" # msg to string pt encode
    for x in msg:
        msg_string += str(x)+'/' # fiecare element din lista il facem string si este concatenat la msg_string
    m_package = buildMsg.package(msg_string,oras)

    sock.sendto(m_package.encode("utf-8"), addr)
    #print("receive response")

    data, addr = sock.recvfrom(1024)
    data_decode = data.decode("utf-8")
    logging.info("From server:", data_decode )

    # print("data_decode:", data_decode)
    message_list = list(data_decode.split("/"))
    #print("message_list:", message_list)
    parsed_message = Parse_Message_Service()
    msg_parsed = parsed_message.Parse(data_decode)
    date_api = list(msg_parsed.payload.split("-"))
    #print("date_api:",date_api)
    #print("temperatura:",date_api[0])
    print("Data primita este", msg_parsed.payload)
    time.sleep(2)
# Inchide conexiune
sock.close()


