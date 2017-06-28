#net = '192.168.1.1'
net = '240.254.358.0'

def validate_ip_func( net ):
	f = 1
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

	if f == 0:
        	return True
	else:
        	return False


print validate_ip_func(net)

#>>> import w6e3
#False
#>>> dir()
#['__builtins__', '__doc__', '__name__', '__package__', 'w6e3']
#>>> w6e3.validate_ip_func('192.168.1.1')
#True
#>>> exit()
#>>> from w6e3 import validate_ip_func
#>>> dir()
#['__builtins__', '__doc__', '__name__', '__package__', 'validate_ip_func', 'w6e3']
#>>> validate_ip_func('248.890.0.0')
#False
#>>> 
