import sys

global binary
binary = []

if len(sys.argv) == 2:
	ip_addr = sys.argv[1]
	list = ip_addr.split('.')
	for i in range(4):
		a = bin(int(list[i]))
		b = a.lstrip('0b')
		while len(b) < 8:
			b = '0' + b
		binary.append(b)
	s = '.'
	result = s.join(binary)
	print "%-20s %-40s" % ("IP address", "Binary")
	print "%-20s %-40s" % (ip_addr, result)			
else:
	print "You have made and error."
