import re

f = open("sw1_cdp.txt")

remote_hosts = []
IPs = []
platform = []

for line in f.readlines():
	s_var = re.search(r"Device ID: (.+)", line)
	if s_var:
		remote_hosts.append(s_var.group(1))
        s_var = re.search(r"IP address: (.+)", line)
	if s_var:
                IPs.append(s_var.group(1))
        s_var = re.search(r"Platform: (.+),", line)
	if s_var:
                platform.append(s_var.group(1))

print "remote_hosts:", remote_hosts
print "         IPs:", IPs
print "    platform:", platform
