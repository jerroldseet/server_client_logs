PART 1:
there are 2 files... server.py and client.py:

server.py is the server
client.py is the client

In client, these are the variable to changed:
- host
    - Host is the ip address of the server
- logs_files
    - log file is the location of the ssh 
- port
    - port is the number port to be use. Please sure that this port number is the same as the server's port number


In server, these are teh variable to be changed:
- PORT
    - port is the number port to be use. Please sure that this port number is the same as the client's port number


PART 2:
I'll be using ansible for this automation as I assume we are using VMs.
For this case I'll be using 