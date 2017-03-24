#!/usr/bin/python
# -*- coding: UTF-8 -*-

import paramiko
from scp import SCPClient

Host = '192.168.31.160'
user = "geh"
passwd = "password"
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(Host, port, user, passwd)
(stdin, stdout, stderr) = ssh.exec_command("killall -9 process_main")
(stdin, stdout, stderr) = ssh.exec_command("ps")
st = stdout.readlines()

scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
remotepath = '/home/geh'
localpath = '/Users/gehui/work/temp/test.txt'
scpclient.put(localpath, remotepath)  # 上传到服务器指定文件
localpath1 = '/Users/gehui/work/temp/get.txt'
scpclient.get(remotepath, localpath1)  # 从服务器中获取文件
ssh.close()
for index, tt in enumerate(st):
    print(index, tt)

