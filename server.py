import socket
import time

# Host suppose to be empty as it's is pointing to itself
HOST = ''    
# Port that both client and server will be using
PORT = 12345 

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            # print("start listening at port {port}".format(port= PORT))
            conn, addr = s.accept()
            with conn:
                # print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print("{addr} has {data} attempt".format( addr = addr[0],data=data.decode("utf-8")))
                    conn.sendall(b'Received')
        except:
            print("Port not closed, waiting to close...")
            time.sleep(1)
