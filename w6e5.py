from w6e3 import validate_ip_func
from w6e4 import dec_to_bin_func 

network = raw_input("Enter the network: ")

if validate_ip_func(network):
	print dec_to_bin_func(network)
else:
	print "IP address is invalid"

