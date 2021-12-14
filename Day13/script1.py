def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

data = read_data("input2a.txt")
# print(data)
xx = 655
yy = 7
dots = [pair.split(",") for pair in data]
# print(dots)

# my_set = set()
# for dot in dots:
#     x = int(dot[0])
#     y = int(dot[1])
#     if y < 7:
#         my_set.add(str(x)+","+str(y))
#     else:
#         my_set.add(str(x)+","+str(14-y))

# print(len(my_set))


my_set = set()
for dot in dots:
    x = int(dot[0])
    y = int(dot[1])
    if x < 655:
        my_set.add(str(x)+","+str(y))
    else:
        my_set.add(str((2*655)-x)+","+str(y))

print(len(my_set))