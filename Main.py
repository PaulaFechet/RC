
from client import Client_request
from Get import Get_Weather_Data
from Message_Header import Message_Header
from Parse_Message_Service import Parse_Message_Service

import socket

# app- conectare la api si preia de acolo date- temperatura in functie de numele
#orasului introdus de client de la tastatura
App=Get_Weather_Data()

#clientul face request intoducand orasul  pt care doreste sa afle vremea
print("\nclient: ")
C=Client_request()

#obtinem data introdusa de client de la tastatura
locatie=C.request()

#obtinem data despre vreme
json, temperatura_celsius=App.get_data(locatie)


print("\n Date format JSON: "+str(json))
print("\nTemperatura :" ,temperatura_celsius, "°C")

temp_fahrenheit=App.convert_to_Fahrenheit(temperatura_celsius)
print("\nTemperatura :" ,temp_fahrenheit, "°F")

header=Message_Header()
binaryString=header.BuildMessage(1, 2, 4, 0, 1, 31)
header.Print()
print(binaryString)

parsed_message= Parse_Message_Service()
msg_parsed=parsed_message.Parse(binaryString)
print("PRESS CTRL-C TO EXIT THE PROG...")
try:
    while True:
        pass
except KeyboardInterrupt:
    print ("Exiting")
    exit(0)






