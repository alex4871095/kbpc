#!/usr/bin/env python

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


def main():
	test_ip = IPAddress('192.168.189.217')
	test_ip.display_in_binary()
	test_ip.display_in_hex()
	print test_ip.is_valid()

if __name__ == '__main__':
        main()


