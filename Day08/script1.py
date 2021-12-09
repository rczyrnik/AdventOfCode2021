# DOESNT WORK, used Sheets instead

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

input_string = read_data("input3.csv")#[1].split()

# print(input_string)

unique_count = 0
for i, line in zip(range(len(input_string)), input_string):
    if i%2 == 0:
        # print(line)
        for string in line.split(" "):

            if(len(string) in (2, 4, 3, 7)):
                # print(string, len(string))
                unique_count += 1

print(unique_count)