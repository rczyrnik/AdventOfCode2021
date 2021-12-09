# same as script2 but with a brute force approach

# ~~ - ~~ - imports - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
from collections import Counter
import itertools
from itertools import permutations

# ~~ - ~~ - functions - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def get_input(line):
    return line.split("|")[0].strip().split(" ")

def get_output(line):
    return line.split("|")[1].strip().split(" ")

def get_decoder_dicts():
    letters = ['a','b','c','d','e','f','g']
    positions = ["A","B","C","D","E","F","G"]

    decoder_dicts = []
    permut = itertools.permutations(letters, len(positions))
    for comb in permut:
        decoder_dicts.append({a:b for a, b in list(zip(comb, positions))})    
    return(decoder_dicts)

def find_right_decoder_dict(input_list):
    for decoder_dict in decoder_dicts:
        count = 0
        for string in input_list:
            decoded_string = ''.join(sorted([decoder_dict[letter] for letter in string]))
            if decoded_string in possible_positions_set:
                count += 1
        if count == 10: return(decoder_dict)

def decode_output(output_list, decoder_dict):
    final_number = ""
    for string in output_list:
        decoded_string = ''.join(sorted([decoder_dict[x] for x in list(string)]))
        final_number += positions_to_numbers_dict[decoded_string]
    return(int(final_number))

# ~~ - ~~ - program - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
lines = read_data("input3.csv")

positions_to_numbers_dict = {'ABCDEF': '0','BC': '1',     'ABDEG': '2',  'ABCDG': '3',
                             'BCFG':'4',   'ACDFG': '5',  'ACDEFG': '6',
                             'ABC': '7',   'ABCDEFG': '8','ABCDFG': '9'}

possible_positions_set = positions_to_numbers_dict.keys()

my_sum = 0
for line in lines:
    input_list = get_input(line) 
    output_list = get_output(line)
    decoder_dicts = get_decoder_dicts()
    decoder_dict = find_right_decoder_dict(input_list)
    my_sum += decode_output(output_list, decoder_dict)

print(my_sum)
