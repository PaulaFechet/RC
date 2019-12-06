from Message_Header import Message_Header

class Parse_Message_Service():
    def __init__(self):
        pass

    def Parse(self,BinaryString):
        message_header = Message_Header()
        message_header.VERSION = int(BinaryString[0:2] ,2)
        print("\nmessage_header.VERSION:", message_header.VERSION)
        message_header.TYPE = int(BinaryString[2:4],2)
        print("\nmessage_header.TYPE:" ,message_header.TYPE)
        message_header.TOKEN_LENGTH = int(BinaryString[4:8],2)
        print("\nmessage.token_length:", message_header.TOKEN_LENGTH)
        message_header.CLASS = BinaryString[8:11]
        print("\nmessage_header.CLASS: ", message_header.CLASS)
        message_header.CODE = BinaryString[11:16]
        print("\n message_header.CODE: ", message_header.CODE)
        message_header.MESSAGE_ID = BinaryString[16:32]
        print("\nmessage_header. MESSAGE_ID", message_header.MESSAGE_ID)
        message_header.token = BinaryString[32: int(message_header.TOKEN_LENGTH)*8]
        print("\nmessage_header.TOKEN: ", message_header.token)

        return message_header

