from Message_Header import Message_Header

class Parse_Message_Service():
    def __init__(self):
        pass

    def Parse(self,BinaryString):
        message_list = list(BinaryString.split("/"))
       # print("message_list:",message_list)
        message_header = Message_Header()
        message_header.VERSION = message_list[0]
       # print("\nmessage_header.VERSION:", message_header.VERSION)
        message_header.TYPE = message_list[1]
       # print("\nmessage_header.TYPE:" ,message_header.TYPE)
        message_header.TOKEN_LENGTH = message_list[2]
       # print("\nmessage.token_length:", message_header.TOKEN_LENGTH)
        message_header.CLASS = message_list[3]
        #print("\nmessage_header.CLASS: ", message_header.CLASS)
        message_header.CODE = message_list[4]
       # print("\n message_header.CODE: ", message_header.CODE)
        message_header.MESSAGE_ID = message_list[5]
       # print("\nmessage_header. MESSAGE_ID", message_header.MESSAGE_ID)

        if message_header.TOKEN_LENGTH:
            message_header.token = message_list[6]
        else:
            message_header.token = None
       # print("\nmessage_header.TOKEN: ", message_header.token)
        payload_code = message_list[7]
        message_header.payload = payload_code[3:]
       # print("\nmessage_header.payload: ", message_header.payload)
        return message_header


