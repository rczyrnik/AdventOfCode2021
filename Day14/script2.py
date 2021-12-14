from collections import Counter
from collections import defaultdict
from itertools import permutations
template = list("CBNBOKHVBONCPPBBCKVH")
# template = list("NNCB")

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

# --------------------------------------------------------------------------------
letters = "NCBHNCBH"
letters = "CBNBOKHVBONCPPBBCKVH"
letters = "NHKOBPCVFSNHKOBPCVFS"
# print(''.join(set(letters)))
counter_dict = {a+b:0 for a, b in list(permutations(letters,2))}


steps = read_data("input2b.txt")

step_dict = {}
for step in steps:
    a, b = step.split(" -> ")
    step_dict[a] = [a[0]+ b, b+a[1]]
# print(step_dict)
# print(counter_dict)

# first setup
for i in range(len(template)-1):
        temp_string = template[i]+template[i+1]
        counter_dict[temp_string] += 1
print(counter_dict)

step_count = 40
for x in range(step_count):
    print("\nSTEP ", x)
    new_counter_dict = counter_dict.copy()
    for old_pair, old_pair_count in counter_dict.items():
        new_pair_1 = step_dict[old_pair][0]
        new_pair_2 = step_dict[old_pair][1]

        print(old_pair, old_pair_count, "--> ", new_pair_1, " ", new_pair_2, end = " ")

        new_counter_dict[old_pair] -= old_pair_count
        new_counter_dict[new_pair_1] += old_pair_count      
        new_counter_dict[new_pair_2] += old_pair_count 
        print(new_counter_dict)
    print()
    counter_dict = new_counter_dict.copy()


# decode
final_dict = {}
for letter in letters:
    final_dict[letter] = 0
# print(final_dict)


for key, value in counter_dict.items():
    for letter in key:
        final_dict[letter] += value
print()
# print(counter_dict)
# print(final_dict)
for key, value in final_dict.items():
    print(key, value, value/2)

# N 2254408979138 1127204489569
# H 8879064643469 4439532321735
# K 6856005831024 3428002915512
# O 5843581309964 2921790654982
# B 7406994199894 3703497099947
# P 1501501801102  750750900551
# C 2857035992125 1428517996063
# V 1358439237716  679219618858
# F 2499074694118 1249537347059
# S 2325335166938 1162667583469

# 4439532321735 - 679219618858

# H 1230 615.0
# N 413 206.5

# K 918 459.0
# O 880 440.0
# B 1035 517.5
# P 226 113.0
# C 436 218.0

# F 480 240.0
# S 366 183.0
# V 160 80.0


# N 864   865
# C 298   298
# B 1748  1749
# H 161   161
# {'NC': 11, 'NB': 10, 'NH': 0, 'NN': -9, 'CN': 0, 'CB': 1, 'CH': 10, 'CC': 0, 'BN': 0, 'BC': 0, 'BH': 10, 'BB': 0, 'HN': 0, 'HC': 0, 'HB': 0, 'HH': 0}

# print()
#     #     # print(template[i]+template[i+1])
    #     new_template.append(template[i])
    #     if template[i]+template[i+1] in step_dict:
    #         new_template.append(step_dict[template[i]+template[i+1]])
    # template = new_template + ['X']
    # print(','.join(template))
    # print(Counter(template)) 


