from collections import defaultdict

def get_map_dict(data):
    map_dict = defaultdict(list)

    for line in data:
        split_line = line.split("-")
        if split_line[1] != "start" and split_line[0] != "end":
            map_dict[split_line[0]].append(split_line[1])
        if split_line[0] != "start" and split_line[1] != "end":
            map_dict[split_line[1]].append(split_line[0])
    return(map_dict)

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def add_step(path_list):
    new_path_list = []
    flag = False
    for path in path_list:
        if path[-1] == "end":
            new_path_list.append(path)
        else:
            for choice in map_dict[path[-1]]:
                if choice.lower() == choice and choice in path:
                    pass
                else:
                    new_path_list.append(path + [choice])
                    flag = True
    return(new_path_list, flag)


data = read_data("input1.txt")

map_dict = get_map_dict(data)
print(map_dict)
path_list = [["start"]]

flag = True
while flag:
    path_list, flag = add_step(path_list)



print("\n\n",len(path_list))
