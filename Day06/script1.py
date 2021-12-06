def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

fish_age_list = [int(x) for x in read_data('input2.csv')[0].split(",")]

def update_fish(age):
    print(age)

def new_day(fish_age_list):
    new_fish_age_list = []
    for fish_age in fish_age_list:
        if fish_age == 0:
            new_fish_age_list.append(6)
            new_fish_age_list.append(8)
        else:
            new_fish_age_list.append(fish_age - 1)
    return new_fish_age_list

for i in range(80):
    fish_age_list = new_day(fish_age_list)

print(i+1, len(fish_age_list))