
def dec_to_bin_func( ip_addr ):
	binary = []
	list = ip_addr.split('.')
	for i in range(4):
		a = bin(int(list[i]))
		b = a.lstrip('0b')
		while len(b) < 8:
			b = '0' + b
		binary.append(b)
	s = '.'
	return s.join(binary)

print dec_to_bin_func('192.168.189.174')

