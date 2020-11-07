#!/usr/bin/env python

import re
import math

from socket import inet_ntoa
from struct import pack

class IPAddress(object):
	def __init__(self, ip_addr):
		self.ip_addr = ip_addr

	def display_in_binary(self):
		splitted_addr = self.ip_addr.split('.')
		for i in range(len(splitted_addr)):
			ob = bin(int(splitted_addr[i]))
			splitted_addr[i] = ob
		js = '.'
		str = js.join(splitted_addr)	
		print str
	
	def display_in_hex(self):
                splitted_addr = self.ip_addr.split('.')
                for i in range(len(splitted_addr)):
                        oh = hex(int(splitted_addr[i]))
                        splitted_addr[i] = oh.lstrip('0x')
                js = '.'
                str = js.join(splitted_addr)    
                print str

	def is_valid(self):
		f = 1
		splitted_addr = self.ip_addr.split('.')
		if len(splitted_addr) == 4:
        		try:
				o1 = int(splitted_addr[0])
        			o2 = int(splitted_addr[1])
        			o3 = int(splitted_addr[2])
        			o4 = int(splitted_addr[3])
			except ValueError:
				return False
        		if o1 > 0 and o1 < 224 and o1 != 127:
                		if o3 >= 0 and o3 <= 255 and o4 >= 0 and o4 <= 255:
                        		if o1 == 169 and o2 == 254:
                                		f = 1
                        		else:
                                		f = 0
                		else:
                        		f = 1
        		else:
                		f = 1

		else:
        		f = 1

		if f == 0:
        		return True
		else:
        		return False


class IPAddressWithNetmask(IPAddress):
	def __init__(self, prefix):
                prefix_split = re.search(r"(.+)/(\d+)", prefix)
                self.netmask = prefix_split.group(2)
		IPAddress.__init__(self, prefix_split.group(1))

	def netmask_in_dotdecimal(self):
		mask = int(self.netmask)
    		
		#bits = 0
    		#for i in xrange(32-mask,32):
        	#	bits |= (1 << i)
    		#return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

		bits = 0xffffffff ^ (1 << 32 - mask) - 1
		return inet_ntoa(pack('>I', bits))
	
def main():
	test_ip2 = IPAddressWithNetmask('192.168.189.217/19')
	print "ip_addr", test_ip2.ip_addr
	print "netmask", test_ip2.netmask
	test_ip2.display_in_binary()
	test_ip2.display_in_hex()
	print test_ip2.is_valid()
	print test_ip2.netmask_in_dotdecimal()

if __name__ == '__main__':
        main()


