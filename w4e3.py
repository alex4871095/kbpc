uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

list1 = uptime1.split(' ')
list2 = uptime2.split(' ')
list3 = uptime3.split(' ')
list4 = uptime4.split(' ')

def strip_list ( list ):
	for i in range(len(list)):
        	y = list[i]
		z = y.strip(',')
		list[i] = z
		y = list[i]
		z = y.strip('s')
		list[i] = z
	return list

list1 = strip_list(list1)
list2 = strip_list(list2)
list3 = strip_list(list3)
list4 = strip_list(list4)

#print list1, "\n", list2, "\n", list3, "\n", list4

def uptime_in_seconds( list ):

	uptime = 0

	try:
		try:
			y = list.index('year')
			years = int(list[y-1]) * 31536000
			uptime = uptime + years
		except ValueError:
			pass
			#print "No years"
		try:
			y = list.index('week')
        		weeks = int(list[y-1]) * 604800
			uptime = uptime + weeks
        	except ValueError:
			pass
			#print "No weeks"
		try:
			y = list.index('day')
        		days = int(list[y-1]) * 86400
			uptime = uptime + days
		except ValueError:
			pass
			#print "No days"
		try:
        		y = list.index('hour')
        		hours = int(list[y-1]) * 3600
			uptime = uptime + hours
        	except ValueError:
			pass
			#print "No hours"
	
		y = list.index('minute')
        	minutes = int(list[y-1]) * 60
		uptime = uptime + minutes
	except ValueError:
		print "Str to integer conversion error"

	return uptime

dict = {list1[0]: "", list2[0]: "", list3[0]: "", list4[0]: ""}

dict['twb-sf-881'] = uptime_in_seconds(list1)
dict['3750RJ'] = uptime_in_seconds(list2)
dict['CATS3560'] = uptime_in_seconds(list3)
dict['rtr1'] = uptime_in_seconds(list4)

print dict

