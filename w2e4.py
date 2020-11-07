cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

list = cisco_ios.split(' ')
index = list.index('Version')
ios_version = list[index+1]
#ios_version.rstrip(",")
ios_version = ios_version[:-1]
print "ios_version = ", ios_version
