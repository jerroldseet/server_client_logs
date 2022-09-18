import socket
import os
import subprocess
import time

# IP address of the server
host = '127.0.0.1'
# The ssh server files
logs_files = "/var/log/auth.log"
logs_files = "/Users/jerrold.seet/Downloads/test_file/auth.log"
# Port that both client and server will be using
port = 12345 

def send_data():

    while True:
        time.sleep(0.5)
        f = open(logs_files, "r")
        num_of_attempt = 0
        for x in f:
            num_of_attempt = num_of_attempt + 1
        print(num_of_attempt)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.sendall(bytes("{num_of_attempt}".format(num_of_attempt = num_of_attempt), 'utf8')) 
            data = s.recv(1024)
            s.close()
            print('Received', repr(data))
        except:
            print("Port not open, waiting...")
            time.sleep(1)

if __name__ == '__main__':
    send_data()