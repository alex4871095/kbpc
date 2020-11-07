output = '''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
'''

list = []
raw_list = output.split('\n')
for i in range(len(raw_list)):
	str = raw_list[i]
	new_list = str.split(' ')
	for y in range(len(new_list)):
		list.append(new_list[y])	

i = 0
z = len(list)
while i < z:
	y = list[i]
	while y == '':
		list.pop(i)
		z = z - 1
		if z == i:
			break
		y = list[i]
	i = i + 1

#print list

dict = {'vendor': '', 'model': '', 'os_version': '', 'uptime': '', 'serial_number': ''}

y = list.index('Cisco')
dict['vendor'] = list[y]
y = list.index('processor')
dict['model'] = list[y-2]
y = list.index('Version')
dict['os_version'] = list[y+1]
y = list.index('uptime')
z = list.index('returned')
s = ' '
dict['uptime'] = s.join(list[y+2:z-1])
y = list.index('SN')
dict['serial_number'] = list[y+4]

print dict
 

