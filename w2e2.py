net = raw_input("Enter the network: ")
splitted_net = net.split('.')
ob1 = bin(int(splitted_net[0]))
ob2 = bin(int(splitted_net[1]))
ob3 = bin(int(splitted_net[2]))
ob4 = bin(int(splitted_net[3]))
o1 = "first_octet"
o2 = "second_octet"
o3 = "fird_octet"
o4 = "fourth_octet"
print "%-15s %-15s %-15s %-15s" % (o1, o2, o3, o4)
print "%-15s %-15s %-15s %-15s" % (ob1, ob2, ob3, ob4)

