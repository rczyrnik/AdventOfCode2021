from collections import Counter
template = list("CBNBOKHVBONCPPBBCKVHX")
# template = list("NNCBX")

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

steps = read_data("input2b.txt")

step_dict = {}
for step in steps:
    a, b = step.split(" -> ")
    step_dict[a] = b
# print(step_dict)

step_count = 10
for x in range(step_count):
    new_template = []
    for i in range(len(template)-1):
        # print(template[i]+template[i+1])
        new_template.append(template[i])
        if template[i]+template[i+1] in step_dict:
            new_template.append(step_dict[template[i]+template[i+1]])
    template = new_template + ['X']
print(Counter(template)) 
# print(list(("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"))  
# print(3950 - 644)
# Counter({'H': 3950, 'B': 3387, 'K': 3102, 
# 'O': 2639, 
# 'C': 1438, 
# 'F': 1247, 
# 'S': 1117, 
# 'N': 1107, 
# 'P': 826, 
# 'V': 644, 'X': 1})