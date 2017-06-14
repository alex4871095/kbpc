entry1 = "* 1.0.192.0/18   157.130.10.233   0 701 38040 9737 i"
entry2 = "* 1.1.1.0/24     157.130.10.233   0 701 1299 15169 i"
entry3 = "* 1.1.42.0/24    157.130.10.233   0 701 9505 17408 2.1465 i"
entry4 = "* 1.0.192.0/19   157.130.10.233   0 701 6762 6762 6762 6762 38040 9737 i"

print "%-20s %-60s" % ("ip_prefix", "as_path")

#for i in (range 4)

list1 = entry1.split(' ')
as_start_index = list1.index('701')
prefix = list1[1]
as_path = list1[as_start_index:-1]
print "%-20s %-60s" % (prefix, as_path)

list2 = entry2.split(' ')
as_start_index = list2.index('701')
prefix = list2[1]
as_path = list2[as_start_index:-1]
print "%-20s %-60s" % (prefix, as_path)

list3 = entry3.split(' ')
as_start_index = list3.index('701')
prefix = list3[1]
as_path = list3[as_start_index:-1]
print "%-20s %-60s" % (prefix, as_path)

list4 = entry4.split(' ')
as_start_index = list4.index('701')
prefix = list4[1]
as_path = list4[as_start_index:-1]
print "%-20s %-60s" % (prefix, as_path)

