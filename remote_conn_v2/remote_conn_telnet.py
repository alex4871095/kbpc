#!/usr/bin/env python

import time
import socket
import telnetlib

def telnet_connection(ip, username, password, commands):
        TELNET_PORT = 23
        TELNET_TIMEOUT = 5
        READ_TIMEOUT = 5
        RESPONSE = ""

	try:
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

                print ip, "connection successful"

        	commands_list = commands.split(",")

        	for command in commands_list:
                	remote_conn.write(command + "\n")
                	time.sleep(2)
                	output = remote_conn.read_very_eager()
                	RESPONSE = RESPONSE + output

        	remote_conn.close()

        except socket.error:
                print ip, "connection problem"

	#print RESPONSE
        return RESPONSE

def main():

        ip = '192.168.0.1'
        username = 'cisco'
        password = ''
        command = 'show ip cef summary,show platform hardware capacity forwarding,show bgp ipv4 unicast summary,show bgp vpnv4 unicast all summary'

	with open('show_scale.txt', 'wb') as f:
        	f.write(telnet_connection(ip, username, password, command))


if __name__ == "__main__":
        main()


