from collections import Counter

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

fish_age_list = [int(x) for x in read_data('input2.csv')[0].split(",")]

fish_age_dict = Counter(fish_age_list)


def new_day(fish_age_dict):
    new_fish_age_dict = {}
    for age in range(8):
        new_fish_age_dict[age] = fish_age_dict[age+1]
    new_fish_age_dict[6] += fish_age_dict[0]
    new_fish_age_dict[8] = fish_age_dict[0]
    return(new_fish_age_dict)

def get_fish_count(fish_age_dict):
    fish_count = 0
    for age in range(9):
        fish_count += fish_age_dict[age]
    return(fish_count)

for day in range(256):
    fish_age_dict = new_day(fish_age_dict)

print("fish count: {}".format(get_fish_count(fish_age_dict)))
