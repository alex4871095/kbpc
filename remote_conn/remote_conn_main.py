#!/usr/bin/env python

import pickle
from remote_conn_telnet import telnet_connection
from remote_conn_ssh import ssh_connection
from show_version_parser import parser

class NetworkObject(object):
	def __init__(self, parsed_dict):
		self.ip = parsed_dict['ip']
		self.username = parsed_dict['username']
		self.password = parsed_dict['password']
		self.hostname = parsed_dict['hostname']
		self.vendor = parsed_dict['vendor']
		self.model = parsed_dict['model']
		self.os_version = parsed_dict['os_version']
		self.serial_number = parsed_dict['serial_number']
		self.uptime = parsed_dict['uptime']

def main():

        ip = ['192.168.0.1']
        username = 'cisco'
        password = 'password'
        method = 'telnet'
        command = 'show version'

	for dev in ip:
        	if method == 'telnet':
        		response_string = telnet_connection(dev, username, password, command)
        	else:
        		response_string = ssh_connection(dev, username, password, command)

                parsed_data = parser(ip, username, password, response_string)
        #        print parsed_data

        network_object = NetworkObject(parsed_data)

	with open('collected_data.txt', 'wb') as f:
        	pickle.dump(network_object, f)

        #f.close()

        with open('collected_data.txt', 'rb') as f:
                network_object = pickle.load(f)
	        print network_object.ip
        	print network_object.username
        	print network_object.password
        	print network_object.hostname
        	print network_object.vendor
        	print network_object.model
        	print network_object.os_version
        	print network_object.serial_number
        	print network_object.uptime

        #f.close()

if __name__ == "__main__":
        main()



