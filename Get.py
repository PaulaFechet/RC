import socket
import json

class Get_Weather_Data():
    def __init__(self):
        pass

    def get_data(self, data_client):
        ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            socket.setdefaulttimeout(4)
            ss.connect(("api.openweathermap.org", 80))
        except socket.error as ex:
            print(ex)
            print("eroare la conexiune!")
            print("\n")
            con_error = "eroare la conexiunea de internet"
            #conn.sendall(con_error.encode("utf-8"))
            #sys.exit()
        request = "GET /data/2.5/weather?q=" + data_client + "&APPID=8a999283783fff58a906c31b2e47a26d&units=metric HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
        # fac array de bytes din string pentru a fi trimis catre client cu encode
        req = request.encode("utf-8")
        # trimit la client
        ss.sendall(req)

        # primesc ce a introdus clientul de la tastatura (eg : numele orasului)
        res = ss.recv(5000)
        # transform in array de bytes cu decode
        res_decode = res.decode("utf-8")

        find_res = res_decode.rfind('\n')
        d = json.loads(res[find_res:])
        try:
            temp = d['main']['temp']
            temp_str = str(temp)
            print(temp)
            temp_b = temp_str.encode("utf-8")
            #conn.sendall(temp_b)
        except KeyError:
            print("error code- ", d["cod"])
            print("description -", d["message"])
            #conn.sendall(d["message"].encode("utf-8"))

        return d, temp

    def convert_to_Fahrenheit(self, temperatura):

        print("Temperatura in Fahrenheit este: " ,temperatura*9/5+32,"°F")
        temp = temperatura * 9 / 5 + 32
        return temp



