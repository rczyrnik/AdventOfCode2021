# ~~ - ~~ - imports - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
from collections import Counter

# ~~ - ~~ - functions - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]




data = read_data("input1.txt")

def get_shortened_line(line):
    my_diff = 10
    while my_diff > 0:
        line_len_start = len(line)
        line = line.replace("()","")
        line = line.replace("[]","")
        line = line.replace("{}","")
        line = line.replace("<>","")
        line_len_end = len(line)
        my_diff = line_len_start - line_len_end
    return(line)

def get_bad_character(shortened_line):
    for my_char in list(shortened_line):
        if my_char in [ "]","}",">",")" ]:
            return(my_char)
    return("x")


my_dict = {"[":"]","(":")","{":"}","<":">"}
money_dict = {")":3,"]":57,"}":1197,">":25137,"x":0}

my_sum = 0
for line in data:
    shortened_line = get_shortened_line(line)

    # if shortened_line:
    bad_char = get_bad_character(shortened_line)

    if bad_char = "x":
        print(shortened_line)
        
    my_sum += money_dict[bad_char]
print(my_sum)