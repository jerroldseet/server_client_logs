import json
import subprocess
import paramiko
import os

json_file = "./vm_list.json"
user_client = "root"
user_server = "root"
root_folder = "./"

def json_converter(file):
    json_file = open(file)
    data = json.load(json_file)
    return data

def main():
    print("hello world")
    servers_client_list = json_converter(json_file)
    server_list = servers_client_list['servers']
    client_list = servers_client_list['clients']
    
    for server in server_list:
        print("server: {server}".format(server=server))
        print("copying script to server vm")
        command = ['scp', '-r', '{root_folder}'.format(root_folder=root_folder), '{user_server}@{server}:/opt/server'.format(user_server=user_server,server=server)]
        subprocess.run(command, capture_output=True)
        print("Script copied")
        print("Executing the script")
        command = 'ssh {user_server}@{server} "python3 -u /opt/server/server.py >> /opt/server/output 2>> /opt/server/error < /dev/null &"'.format(user_server=user_server,server=server)
        os.system(command)
        

    for client in client_list:
        print("client: {client}".format(client=client))
        print("copying script to client vm")
        command = ['scp', '-r', '{root_folder}'.format(root_folder=root_folder), '{user_client}@{client}:/opt/client'.format(user_client=user_client,client=client)]
        subprocess.run(command, capture_output=True)
        print("Script copied")
        print("Executing the script")
        command = 'ssh {user_client}@{client} "python3 -u /opt/client/client.py >> /opt/client/output 2>> /opt/client/error < /dev/null &"'.format(user_client=user_client,client=client)
        os.system(command)

if __name__ == '__main__':
    main()