def list_to_dict_func( list):
	dict = {}
	for i in range(len(list)):
		dict[i] = list[i]
	return dict

#list = range(10)
list = ['one', 'two', 'three']

print list_to_dict_func(list)

