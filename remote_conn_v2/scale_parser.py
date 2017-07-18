#!/usr/bin/env python

import re

def parser (ip, response_string):

        network_device = {}

        network_device['ip'] = ip

        hostname = re.search(r"(.+)#", response_string)
        if hostname:
                network_device['hostname'] = hostname.group(1)

        prefixes = re.search(r"(.+) prefixes", response_string)
        if prefixes:
                network_device['cef_prefixes'] = prefixes.group(1).lstrip(' ')

        tcam_v4 = re.search(r"72 bits \(IPv4, MPLS, EoM\) (.+) (\d+?) (.+)", response_string)
        if tcam_v4:
                network_device['tcam_v4_q'] = tcam_v4.group(2)
                tcam_v4_p = tcam_v4.group(3).lstrip(' ')
                tcam_v4_p = tcam_v4_p.rstrip('\r')
		network_device['tcam_v4_p'] = tcam_v4_p
		
        tcam_v6 = re.search(r"144 bits \(IP mcast, IPv6\) (.+) (\d+?) (.+)", response_string)
        if tcam_v6:
                network_device['tcam_v6_q'] = tcam_v6.group(2)
                tcam_v6_p = tcam_v6.group(3).lstrip(' ')
		tcam_v6_p = tcam_v6_p.rstrip('\r')
		network_device['tcam_v6_p'] = tcam_v6_p

        bgp_ipv4 = re.search(r"show bgp ipv4 unicast summary\r\n(.+)\r\n(.+)\r\n(\d+?) network entries", response_string)
        if bgp_ipv4:
                network_device['bgp_ipv4'] = bgp_ipv4.group(3)
	else:
		network_device['bgp_ipv4'] = ""

        bgp_vpnv4 = re.search(r"show bgp vpnv4 unicast all summary\r\n(.+)\r\n(.+)\r\n(\d+?) network entries", response_string)
        if bgp_vpnv4:
                network_device['bgp_vpnv4'] = bgp_vpnv4.group(3)
	else:
		network_device['bgp_vpnv4'] = ""

	#print network_device
	return network_device

def main():

        ip = '192.168.0.1'

	with open('show_scale.txt', 'r') as f:
        	response_string = f.read()

        print parser(ip, response_string)


if __name__ == "__main__":
        main()

