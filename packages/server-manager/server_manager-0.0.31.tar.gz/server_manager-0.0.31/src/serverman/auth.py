import os
import subprocess

users = os.popen('cat /etc/passwd').read().split('\n')
valid_users = []
readable_valid_user_data = []

for i in users:
    if "nologin" in i or "false" in i or i == "":
        #print("nologin")
        pass
    else:
        valid_users.append(i)


for j in valid_users:
    base_string = j.split(':')
    individual_user_data = {
        "username": base_string[0],
        "user_id": f"{base_string[2]}:{base_string[3]}",
        "home_dir": base_string[5],
        "shell": base_string[6],
    }
    readable_valid_user_data.append(individual_user_data)

def authenticate(username, password, cmnd):
    cmd = ['su', '-', username, '-c', cmnd]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.communicate(input=password.encode() + b'\n')[0]
    return output

#print(readable_valid_user_data)