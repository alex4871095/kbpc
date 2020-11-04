import re

f = open("r1_cdp.txt")
dict = {}

for line in f.readlines():
	s_var = re.search(r"Device ID: (.+)", line)
	if s_var:
		dict['hostname'] = s_var.group(1)
        s_var = re.search(r"IP address: (.+)", line)
	if s_var:
                dict['ip'] = s_var.group(1)
        s_var = re.search(r"Platform: (.+?) (.+?),  Capabilities: (.+?) ", line)
	if s_var:
                dict['vendor'] = s_var.group(1)
		dict['model'] = s_var.group(2)
		dict['device_type'] = s_var.group(3)

print dict
