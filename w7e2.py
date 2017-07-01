import re

f = open("ospf_single_interface.txt")
dict = {}

for line in f.readlines():
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
print "Hello:", dict['Hello']
print " Dead:", dict['Dead']
