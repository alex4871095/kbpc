net = raw_input("Enter the network: ")
splitted_net = net.split('.')
if len(splitted_net) == 3:
	splitted_net.append('0')
if len(splitted_net) == 4:
	splitted_net[-1] = '0'
s = '.'
print "Entered network is", s.join(splitted_net)
first_octet_bin = bin(int(splitted_net[0]))
first_octet_hex = hex(int(splitted_net[0]))
fc = "NETWORK_NUMBER"
sc = "FIRST_OCTET_BINARY"
tc = "FIRST_OCTET_HEX"
print "%-20s %-20s %-20s" % (fc, sc, tc)
print "%-20s %-20s %-20s" % (s.join(splitted_net), first_octet_bin, first_octet_hex)

