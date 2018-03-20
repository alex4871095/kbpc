#!/usr/bin/env python

import pickle
from remote_conn_telnet import telnet_connection
from remote_conn_ssh import ssh_connection
from scale_parser import parser

hosts = '''192.168.0.2
192.168.0.3
192.168.0.4'''

class NetworkObject(object):
	def __init__(self, parsed_data):
		self.ip = parsed_data['ip']
		self.hostname = parsed_data['hostname']
		#self.vendor = parsed_data['vendor']
		#self.model = parsed_data['model']
		#self.os_version = parsed_data['os_version']
		#self.serial_number = parsed_data['serial_number']
		#self.uptime = parsed_data['uptime']
		self.grt_prefixes = parsed_data['cef_prefixes']
		self.tcam_v4_q = parsed_data['tcam_v4_q']
		self.tcam_v4_p = parsed_data['tcam_v4_p']
		self.tcam_v6_q = parsed_data['tcam_v6_q']
		self.tcam_v6_p = parsed_data['tcam_v6_p']
		self.bgp_ipv4 = parsed_data['bgp_ipv4']
		self.bgp_vpnv4 = parsed_data['bgp_vpnv4']
		self.vrf_number = parsed_data['vrf_number']
		self.pw_up = parsed_data['pw_up']
		self.pw_down = parsed_data['pw_down']
		self.pw_stby = parsed_data['pw_stby']
		

def main():

#	tmp = '''
	ip = hosts.split('\n')
        username = 'cisco'
        password = ''
        method = 'telnet'
        command = 'show ip cef summary,show platform hardware capacity forwarding,show bgp ipv4 unicast summary,show bgp vpnv4 unicast all summary,show vrf detail | incl VRF Id,show mpls l2transport summary | incl up'

	f = open('collected_data.txt', 'wb')

	for dev in ip:
        	if method == 'telnet':
        		response_string = telnet_connection(dev, username, password, command)
        	elif method == 'ssh':
        		response_string = ssh_connection(dev, username, password, command)

                parsed_data = parser(dev, response_string)
                #print parsed_data

		try:
       			network_object = NetworkObject(parsed_data)
			pickle.dump(network_object, f)
		except KeyError:
			pass
			#print "Pickling error"
        
	f.close()		
#	'''

	print "%-20s %-20s %-15s %-15s %-15s %-17s %-17s %-17s %-17s %-17s %-17s %-17s %-17s" % ("Hostname", "IP", "CEF GRT pfx", "BGP ipv4 pfx", "BGP vpnv4 pfx", "TCAM v4 usage", "TCAM v4 usage(%)", "TCAM v6 usage", "TCAM v6 usage(%)", "VRF number", "PW up", "PW down", "PW stby") 

	with open('collected_data.txt', 'rb') as f:
		while True:
			try:
                		network_object = pickle.load(f)
        			print "%-20s %-20s %-15s %-15s %-15s %-17s %-17s %-17s %-17s %-17s %-17s %-17s %-17s" % (network_object.hostname, network_object.ip, network_object.grt_prefixes, network_object.bgp_ipv4, network_object.bgp_vpnv4, network_object.tcam_v4_q, network_object.tcam_v4_p, network_object.tcam_v6_q, network_object.tcam_v6_p, network_object.vrf_number, network_object.pw_up, network_object.pw_down, network_object.pw_stby)

			except EOFError:
				break


if __name__ == "__main__":
        main()



