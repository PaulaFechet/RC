'''
        0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Ver| T |  TKL  |      Code     |          Message ID           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |   Token (if any, TKL bytes) ...
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |   Options (if any) ...
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |1 1 1 1 1 1 1 1|    Payload (if any) ...
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   Request/Response Code (8 bits)
0	1	2	3	4	5	6	7
 Class  |	      Code

 COAP_MESSAGE_FORMAT

HEADERUL FORMAT DIN :
1. VERSIUNEA: 2 BITI
2. MESSAGE-TYPE : 2 BITI
3. TOKENLENGTH:4 bit
4. CODE: -code class -3 biti
        -code response -5 biti
        CODE RESPONSE (8 bit)
5. MESSAGE_Id : 16 bit!

EMPTY = <Code 0 “EMPTY”>
GET = <Request Code 1 “GET”>
POST = <Request Code 2 “POST”>
PUT = <Request Code 3 “PUT”>
DELETE = <Request Code 4 “DELETE”>

    Version (VER) (2 bits)
Indicates the CoAP version number.

    Type (2 bits)
This describes the datagram's message type for the two message type context of Request and Response.
Request
0 : Confirmable : This message expects a corresponding Acknowledgement message.
1 : Non-confirmable : This message does not expect a confirmation message.
Response
2 : Acknowledgement : This message is a response that acknowledge a confirmable message
3 : Reset : This message indicates that it had received a message but could not process it.
'''

class Message_Header():
    def __init__(self):
        self.VERSION = 0
        self.TYPE = 0
        self.TOKEN_LENGTH = 0
        self.token=0
        self.CLASS=0

        self.CODE=0
        self.MESSAGE_ID=0
        message = ""

    def BuildMessage(self, VERSION, TYPE, TOKEN_LENGTH, CLASS, CODE, MESSAGE_ID):


        # formatam elementele din header setandu-le dimensiunea
        self.VERSION = format(VERSION, '02b')
        self.TYPE = format(TYPE, '02b')
        self.TOKEN_LENGTH = format(TOKEN_LENGTH, '04b')

        self.CLASS = format(CLASS, '03b')
        self.CODE = format(CODE, '05b')
        self.MESSAGE_ID = format(MESSAGE_ID, '016b')

        message1 = (VERSION) << 6 | TYPE << 4 | TOKEN_LENGTH
        print("version<<6: " ,VERSION<<6)
        print("type<<4 ", TYPE<<4)
        print("TOKEN_LENGTH: ", TOKEN_LENGTH)
        print("message1: ", message1)
        message1 = format(message1, '08b')
        print("message 1: ", message1)
        message2 = (CLASS) << 5 | CODE
        print("CLASS << 5:", CLASS<<5)
        print("CODE : ", CODE)
        message2 = format(message2, '08b')
        message3 = self.MESSAGE_ID


        if(TOKEN_LENGTH>0 and TOKEN_LENGTH<=8):
            self.token=format(self.token,str(self.get_TOKEN_LENGTH()*8)+'b' )

        print("self.token: ", self.token)

        return str(message1)+str(message2)+str(message3)

    def get_TOKEN_LENGTH(self):
        return int(str(self.TOKEN_LENGTH),2)

#tokenul trebuie generat de catre client

    def getVERSION(self):
        return int(str(self.VERSION),2)

    def getType(self):
        return int(str(self.TYPE),2)

    def getCLass(self):
        return int(str(self.CLASS),2)

    def getCode(self):
        return int(str(self.CODE),2)

    def getMessageId(self):
        return int(str(self.MESSAGE_ID),2)




    def Print(self):
        print("\n We are printing the message format....")
        print("\n VERSION: "+ str(self.getVERSION()))
        print("\n TYPE: "+str(self.getType()))
        print("\n CLASS.CODE: "+ (str(self.getCLass())+"."+str(self.getCode())))

        #FOLOSIM MESSAGE ID PENTRU A GASI DUPLICATELE
        #MATCH MESSAGES OF TYPE ACK/RST
        #RESPONSE MESSAGES WILL HAVE THE SAME MESSAGE ID

        print("\n MESSAGE ID: " +str(self.getMessageId()))


'''
The entire code is typically communicated in the form class.code .
Method: 0.XX EMPTY , GET ,POST
Success: 2.XX Created,Deleted,Valid,Changed,Content,Continue
Client Error: 4.XX
Bad Request, Unauthorized, Bad Option, Forbidden ,Not Found, Method Not Allowed, Not Acceptable

Server Error: 5.XX
Internal Server Error,Not Implemented,Bad Gateway,Service Unavailable,Gateway Timeout,Proxying Not Supported
Signaling Codes: 7.XX Unassigned,CSM,Ping,Pong,Release,Abort


EMPTY = <Code 0 “EMPTY”>
GET = <Request Code 1 “GET”>
POST = <Request Code 2 “POST”>
PUT = <Request Code 3 “PUT”>
DELETE = <Request Code 4 “DELETE”>
FETCH = <Request Code 5 “FETCH”>
PATCH = <Request Code 6 “PATCH”>
iPATCH = <Request Code 7 “iPATCH”>
CREATED = <Successful Response Code 65 “2.01 Created”>
DELETED = <Successful Response Code 66 “2.02 Deleted”>
VALID = <Successful Response Code 67 “2.03 Valid”>
CHANGED = <Successful Response Code 68 “2.04 Changed”>

"""
    def set_TOKEN(self, token):
        if token:
            for get_TOKEN_LENGTH in range(1, 8+1):
                if token < (1 << (8*get_TOKEN_LENGTH)):
                    token = get_TOKEN_LENGTH
                    break
            if not token:
                raise ValueError('token {0] too long '.format(token))
"""


'''







