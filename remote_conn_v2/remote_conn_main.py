#!/usr/bin/env python

import pickle
from remote_conn_telnet import telnet_connection
from remote_conn_ssh import ssh_connection
from scale_parser import parser


class NetworkObject(object):
	def __init__(self, parsed_dict):
		self.ip = parsed_dict['ip']
		self.hostname = parsed_dict['hostname']
		#self.vendor = parsed_dict['vendor']
		#self.model = parsed_dict['model']
		#self.os_version = parsed_dict['os_version']
		#self.serial_number = parsed_dict['serial_number']
		#self.uptime = parsed_dict['uptime']
		self.prefixes = parsed_dict['cef_prefixes']
		self.tcam_v4_q = parsed_dict['tcam_v4_q']
		self.tcam_v4_p = parsed_dict['tcam_v4_p']
		self.tcam_v6_q = parsed_dict['tcam_v6_q']
		self.tcam_v6_p = parsed_dict['tcam_v6_p']


def main():

	ip = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
        username = 'cisco'
        password = 'password'
        method = 'telnet'
        command = 'show ip cef summary,show platform hardware capacity forwarding'

	f = open('collected_data.txt', 'wb')

	for dev in ip:
        	if method == 'telnet':
        		response_string = telnet_connection(dev, username, password, command)
        	else:
        		response_string = ssh_connection(dev, username, password, command)

                parsed_data = parser(dev, response_string)
                #print parsed_data

		try:
        		network_object = NetworkObject(parsed_data)
			pickle.dump(network_object, f)
		except KeyError:
			pass
        
	f.close()		

	with open('collected_data.txt', 'rb') as f:
		while True:
			try:
                		network_object = pickle.load(f)
	       			print "Hostname         ", network_object.hostname
        			print "IP               ", network_object.ip
        			print "CEF prefixes     ", network_object.prefixes
				print "TCAM v4 usage    ", network_object.tcam_v4_q
        			print "TCAM v4 usage(%) ", network_object.tcam_v4_p
        			print "TCAM v6 usage    ", network_object.tcam_v6_q
        			print "TCAM v6 usage(%) ", network_object.tcam_v6_p
				print "\n"
			except EOFError:
				break


if __name__ == "__main__":
        main()



