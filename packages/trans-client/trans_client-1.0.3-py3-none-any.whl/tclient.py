#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Author:   fetch150zy
# Mail:     zhewei@stu.xidian.edu.cn


import sys
import os
import subprocess
import json


remote_host = ''
remote_base_path = ''
remote_user = ''


def help():
    print('''\n\033[36m    A tool based on scp for quickly transmitting data on a server. If you
do not want to enter the account password during the transmission process,
please configure the ssh key in advance. This is a client-side script. If
you have set up your own LAN server as a backup server or data transfer
station, you can install the trans-server script on the server side.\033[0m\n\n''')
    
    print('\033[36mPlease use "\033[31mtcl config\033[36m" for simple configuration before use.')
    print('Below are some simple descriptions of configuration options: \033[0m')
    print('     user:  user name')
    print('       ip:  remote ip address')
    print('     path:  remote server root path\n')
    
    print('In /home/user/.trans.cfg: ')
    print('''\033[33m{
    "user": "jack",
    "ip": "192.168.3.55,
    "path": "/home/jack/",
}\033[0m
''')
    
    print('If you want to use tcl to ssh login, please use "\033[31mtcl login\033[0m"\n')
    
    print('\033[31mUsage: tcl [option] <local_path> <remote_path>\033[0m\n')

    print('Option: ')
    print('     \033[34m-g --get\033[0m: get file or dir from the server')
    print('     \033[34m-p --put\033[0m: upload file or dir to the server\n')

    print('Like this: ')
    print('           tcl --get /home/xxx/dir remote_dir')
    print('       or: tcl -g /home/xxx/dir remote_dir')
    print('Copy the user@remote-ip:<remote_base_path>/remote_dir to /home/xxx/dir/\n')

    print('           tcl --put /home/xxx/dir remote-dir')
    print('       or: tcl -p /home/xxx/dir remote_dir')
    print('Copy the /home/xxx/dir to user@remote-ip:<remote_base_path>/remote_dir/\n')


def clean():
    filename = config_filename = os.path.expanduser('~') + '/.trans.cfg'
    if os.path.exists(filename):
        os.remove(filename)


def read_config():
    filename = config_filename = os.path.expanduser('~') + '/.trans.cfg'
    with open(filename, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    global remote_host
    global remote_base_path
    global remote_user
    remote_host = config_data["ip"]
    remote_user = config_data["user"]
    remote_base_path = config_data["path"]


def set_config():
    keys = ["user", "ip", "path"]
    data = {}
    for key in keys:
        value = input(f'{key}: ')
        data[key] = value
    config_filename = os.path.expanduser('~') + '/.trans.cfg'
    with open(config_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def login():
    ssh_command = f'ssh {remote_user}@{remote_host}'
    subprocess.run(ssh_command, shell=True)


def parse():
    local_path = sys.argv[2]
    if not os.path.exists(local_path):
        sys.stderr.write(f'Local path: {local_path} not exist\n')
        sys.exit(1)

    remote_path = remote_base_path + '/' + sys.argv[3]
    cmd = f"ssh {remote_user}@{remote_host} 'test -e {remote_path}'"
    try:
        subprocess.run(cmd, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        sys.stderr.write(f'Remote path: {remote_path} not exist\n')
        sys.exit(1)

    src_path = ''
    dest_path = ''
    if sys.argv[1] in ['-p', '--put']:
        src_path = local_path
        dest_path = remote_user + '@' + remote_host + ':' + remote_path
    elif sys.argv[1] in ['-g', '--get']:
        src_path = remote_user + '@' + remote_host + ':' + remote_path
        dest_path = local_path
    else:
        sys.stderr.write('Option: {sys.argv[1] is invalid\n}')
        sys.exit(1)

    return (src_path, dest_path)


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'config':
            set_config()
        elif sys.argv[1] == 'login':
            read_config()
            login()
        elif sys.argv[1] == 'help':
            help()
        elif sys.argv[1] == 'clean':
            clean()
        else:
            sys.stderr.write('Please use "\033[31mtcl help\033[0m" to learn usage detail\n')
            sys.exit(1)
    elif len(sys.argv) == 4:
        read_config()
        src_path, dest_path = parse()
        try:
            subprocess.run(f'scp -r {src_path} {dest_path}', check=True, shell=True)
            print(f'Success: {src_path} to {dest_path}')
        except subprocess.CalledProcessError:
            sys.stderr.write('Something wrong in running scp\n')
            sys.exit(1)
    else:    
        sys.stderr.write('\033[31mUsage: tcl config\n')
        sys.stderr.write('Usage: tcl login\n')
        sys.stderr.write('Usage: tcl help\n')
        sys.stderr.write('Usage: tcl [option] <local_path> <remote_path>\033[0m\n')
        sys.exit(1)

