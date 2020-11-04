import show_version

with open("./show_version.txt") as show_ver_file:
	show_ver = show_ver_file.read()

print "Version: ", show_version.obtain_version(show_ver)
print "Uptime : ", show_version.obtain_uptime(show_ver)
print "Model  : ", show_version.obtain_model(show_ver)
