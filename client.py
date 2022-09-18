import socket
import os
import subprocess
import time

# IP address of the server
host = '127.0.0.1'
# The ssh server files
logs_files = "/var/log/auth.log"
# Port that both client and server will be using
port = 12345 

def send_data():

    while True:
        time.sleep(0.5)
        print('Finding out the number of ssh logs')
        command = ['cat', logs_files ]
        out = subprocess.run(command, capture_output=True)
        raw_logs = (out.stdout).decode("utf-8") 
        logs = raw_logs.split('\n')
        del logs[-1] #there's always one more array in the end
        print("{len} attempt found".format(len=len(logs)))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.sendall(bytes("{logs}".format(logs = len(logs)), 'utf8')) 
            data = s.recv(1024)
            s.close()
            print('Received', repr(data))
        except:
            print("Port not open, waiting...")
            time.sleep(1)

if __name__ == '__main__':
    send_data()