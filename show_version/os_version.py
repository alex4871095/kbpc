import re

def obtain_version( data_string ):
	os_ver = re.search(r"Version (.+),", data_string)
	if os_ver:
		version = "Version " + os_ver.group(1)
		return version
	else:
		return None

def main():
	with open("../data/show_version.txt") as show_ver_file:
		show_ver = show_ver_file.read()
	print (obtain_version(show_ver))

if __name__ == '__main__':
	main()

