show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

list = []
raw_list = show_ip_int_brief.split('\n')
for i in range(len(raw_list)):
	str = raw_list[i]
	new_list = str.split(' ')
	for y in range(len(new_list)):
		list.append(new_list[y])	

#print len(list)
#print list

i = 0
z = len(list)
while i < z:
	y = list[i]
	while y == '':
		list.pop(i)
		z = z - 1
		#print "z is %s" % (z)
		if z == i:
			break
		y = list[i]
	i = i + 1
	#print "i is %s" % (i)

#print len(list)
#print list

y = 4
tuple = ()
final_list = []
for i in range(13):
	if list[y] == 'up' and list[y+1] == 'up':
		tuple = (list[y-4], list[y-3], list[y], list[y+1])
		#print tuple
		final_list.append(tuple)
	y = y + 6

print final_list

