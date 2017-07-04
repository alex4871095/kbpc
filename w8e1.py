
def validate_ip_func( net ):
	f = 1
	splitted_net = net.split('.')
	if len(splitted_net) == 4:
        	try:
			o1 = int(splitted_net[0])
        		o2 = int(splitted_net[1])
        		o3 = int(splitted_net[2])
        		o4 = int(splitted_net[3])
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


if __name__ == '__main__':
	test_list = ['192.168.1', '10.1.1.', '10.1.1.x', '0.77.22.19', '-1.88.99.17', '241.17.17.9', '127.0.0.1', '169.254.1.9', '192.256.7.7', '192.168.-1.7', '10.1.1.256', '1.1.1.1', '223.255.255.255', '223.0.0.0', '10.200.255.1', '192.168.17.1']
	test_ip_addresses = {}
	for ip in test_list:
		test_ip_addresses[ip] = validate_ip_func(ip)
	print test_ip_addresses


