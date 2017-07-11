#!/bin/env python

import time
import paramiko

def ssh_connection(ip, username, password, commands):

        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        remote_conn_pre.connect(ip, username=username, password=password)

        remote_conn = remote_conn_pre.invoke_shell()
        output = remote_conn.recv(65535)

        commands_list = commands.split(",")

        remote_conn.send("terminal length 0\n")

        for command in commands_list:
                remote_conn.send(command + "\n")
                time.sleep(1)
                output = remote_conn.recv(65535)
                RESPONSE = RESPONSE + output

        remote_conn.close()
        return RESPONSE

def main():

        ip = '213.140.243.131'
        username = 'cisco_tech'
        password = 'rjkktrnjh2014'
        commands = 'show ip cef summary,show version'

        print ssh_connection(ip, username, password, commands)


if __name__ == "__main__":
        main()
