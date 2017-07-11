#!/bin/env python

import time
import telnetlib

def telnet_connection(ip, username, password, commands):
        TELNET_PORT = 23
        TELNET_TIMEOUT = 5
        READ_TIMEOUT = 5
        RESPONSE = ""

        remote_conn = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)

        output = remote_conn.read_until("sername:", READ_TIMEOUT)
        remote_conn.write(username + "\n")

        output = remote_conn.read_until("assword:", READ_TIMEOUT)
        remote_conn.write(password + "\n")

        time.sleep(1)
        output = remote_conn.read_very_eager()

        remote_conn.write("terminal length 0" + "\n")
        time.sleep(1)
        output = remote_conn.read_very_eager()

        commands_list = commands.split(",")

        for command in commands_list:
                remote_conn.write(command + "\n")
                time.sleep(1)
                output = remote_conn.read_very_eager()
                RESPONSE = RESPONSE + output

        remote_conn.close()
        return RESPONSE

def main():

        ip = '213.140.243.131'
        username = 'cisco_tech'
        password = 'rjkktrnjh2014'
        commands = 'show ip cef summary,show version'

        print telnet_connection(ip, username, password, commands)


if __name__ == "__main__":
        main()


