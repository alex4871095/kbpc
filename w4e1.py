f = 1
while f == 1:
	net = raw_input("Enter the network: ")
	splitted_net = net.split('.')
	if len(splitted_net) == 4:
        	o1 = int(splitted_net[0])
        	o2 = int(splitted_net[1])
        	o3 = int(splitted_net[2])
        	o4 = int(splitted_net[3])
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

	print net
	if f == 0:
        	print "IP address is valid"
	else:
        	print "IP address is invalid"



