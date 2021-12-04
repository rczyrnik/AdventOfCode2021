from collections import Counter

def bin_to_dec(binary_string):
	output = 0

	for i in range(len(binary_string)):
		output += int(binary_string[-1-i])*2**i

	return(output)
# print(binary_to_decimal('01010'))

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]


lines = read_data('data2.csv')
oxy_list = lines
co2_list = lines

for i in range(len(lines[0])):

	# get the counts
	oxy_counts = Counter([number[i] for number in oxy_list])
	co2_counts = Counter([number[i] for number in co2_list])

	# find the number to filter on
	if oxy_counts['0'] > oxy_counts['1']: oxy_filter = '0'
	else: oxy_filter = '1'

	if co2_counts['1'] < co2_counts['0']: co2_filter = '1'
	else: co2_filter = '0'

	# create a new list
	new_oxy_list = []
	for number in oxy_list: 
		if number[i] == oxy_filter: new_oxy_list.append(number)

	new_co2_list = []
	for number in co2_list: 
		if number[i] == co2_filter: new_co2_list.append(number)
	
	# new list is now old list
	oxy_list = new_oxy_list
	co2_list = new_co2_list

	# id final numbers
	if len(oxy_list) == 1: oxy_number = oxy_list[0]
	if len(co2_list) == 1: co2_number = co2_list[0]

print(oxy_number, co2_number, bin_to_dec(oxy_number) * bin_to_dec(co2_number))


	
