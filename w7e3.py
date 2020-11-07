import re

def parse_string ( str ):
	list  = re.split(r'(.+is up, line protocol is up)', str)
	list.pop(0)
	#print len(list)
	#print list

	ospf_list = []

	i=0
	while i < len(list):
		if (i+2) <= len(list):
			str = list[i] + list[i+1]
			ospf_list.append(str) 
		i += 2

	#print len(ospf_list)
	#print ospf_list
	list_of_lists = []
	for i in range(len(ospf_list)):
		tmp = ospf_list[i].split('\n')
		list_of_lists.append(tmp) 
	#print list_of_lists
	return list_of_lists

def parse_list ( list ):
	dict = {}
	for line in list:
		s_var = re.search(r"(.+) is up, line protocol is up", line)
		if s_var:
			dict['Int'] = s_var.group(1)
        	s_var = re.search(r"Internet Address (.+?), Area (.+?),", line)
		if s_var:
                	dict['IP'] = s_var.group(1)
			dict['Area'] = s_var.group(2)
        	s_var = re.search(r"Network Type (.+), Cost: (.+)", line)
        	if s_var:
                	dict['Type'] = s_var.group(1)
			dict['Cost'] = s_var.group(2)
        	s_var = re.search(r"Hello (.+), Dead (.+?),", line)
        	if s_var:
                	dict['Hello'] = s_var.group(1)
			dict['Dead'] = s_var.group(2)

	print "  Int:", dict['Int']
	print "   IP:", dict['IP']
	print " Area:", dict['Area']
	print " Type:", dict['Type']
	print " Cost:", dict['Cost']
	if 'Hello' in dict.keys():
		print "Hello:", dict['Hello']
		print " Dead:", dict['Dead']
	print "\n"


f = open("ospf_data.txt")
a = f.read()

list = parse_string (a)
#print list

for i in range(len(list)):
	parse_list (list[i])

