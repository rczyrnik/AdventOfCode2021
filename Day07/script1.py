from collections import Counter

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

crab_position_list = [int(x) for x in read_data('input2.csv')[0].split(",")]
max_position = max(crab_position_list)

pyramid_dict = {0:0, 1:1}

for dist in range(1, max_position+1):
    pyramid_dict[dist] = pyramid_dict[dist-1] + dist

def get_total_fuel(x):
    total_fuel = 0
    for crab_position in crab_position_list:
        total_fuel += pyramid_dict[abs(crab_position - x)]
    return total_fuel

def get_all_possible_fuels():
    possible_fuels = []
    for x in range(max_position):
        possible_fuels.append(get_total_fuel(x))
    return possible_fuels

print(min(get_all_possible_fuels()))
