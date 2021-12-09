from collections import Counter

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

input_string = read_data("input3.csv")#[1].split()


# print(input_string)

unique_count = 0

def find_top(number_list):
    for string in number_list:
        if len(string) == 2:
            two_list = list(string)
        elif len(string) == 3:
            three_list = list(string)

    for letter in two_list:
        three_list.remove(letter)
    return three_list[0]

def find_left_bottom(number_list):
    temp_dict = Counter(''.join(number_list))
    for letter in temp_dict:
        if temp_dict[letter] == 4:
            return(letter)

def find_left_top(number_list):
    temp_dict = Counter(''.join(number_list))
    for letter in temp_dict:
        if temp_dict[letter] == 6:
            return(letter)

def find_right_bottom(number_list):
    temp_dict = Counter(''.join(number_list))
    for letter in temp_dict:
        if temp_dict[letter] == 9:
            return(letter)

def find_right_top(number_list, right_bottom):
    for number in number_list:
        if len(number) == 2:
            temp_list = list(number)
            temp_list.remove(right_bottom)
            return(temp_list[0])
            # return(list(number).remove(right_bottom)[0])

def find_middle(number_list, left_top, right_top, right_bottom):
    for number in number_list:
        if len(number) == 4:
            temp_list = list(number)
            temp_list.remove(left_top)
            temp_list.remove(right_top)
            temp_list.remove(right_bottom)
            return(temp_list[0])
            # return(list(number).remove(right_bottom)[0])


def find_bottom(number_list, top, left_bottom, left_top, right_bottom, right_top, middle):
    for number in number_list:
        if len(number) == 7:
            temp_list = list(number)
            temp_list.remove(left_top)
            temp_list.remove(left_bottom)

            temp_list.remove(right_top)
            temp_list.remove(right_bottom)

            temp_list.remove(top)
            temp_list.remove(middle)   

            return(temp_list[0])
            # return(list(number).remove(right_bottom)[0])



total_sum = 0
for line in input_string:
    number_list = line.split("|")[0].split(" ")
    number_list.remove("")
   
    top = find_top(number_list)
    left_bottom = find_left_bottom(number_list)
    left_top = find_left_top(number_list)
    right_bottom = find_right_bottom(number_list)
    right_top = find_right_top(number_list, right_bottom)
    middle = find_middle(number_list, left_top, right_top, right_bottom)
    bottom = find_bottom(number_list, top, left_bottom, left_top, right_bottom, right_top, middle)

    letter_to_position = {top: "A", 
                    left_top: "B", 
                    left_bottom: "E", 
                    right_top: "C", 
                    right_bottom: "F", 
                    middle: "D", 
                    bottom: "G"}

    # letter_to_position2 = {top: "Atop", 
    #                 left_top: "Bleft_bottom", 
    #                 left_top: "Cleft_top", 
    #                 right_bottom: "Dright_bottom", 
    #                 right_top: "Eright_top", 
    #                 middle: "Fmiddle", 
    #                 bottom: "Gbottom"}

    positions_to_number = {"ABCEFG": 0,
                            "CF": 1,
                            "ACDEG": 2,
                            "ACDFG": 3,
                            "BCDF": 4,
                            "ABDFG": 5,
                            "ABDEFG": 6,
                            "ACF": 7,
                            "ABCDEFG": 8,
                            "ABCDFG": 9}
    
    output_list = line.split("|")[1].split(" ")
    output_list.remove("")

    number_string = ''
    for number in output_list:
        decoded = list(letter_to_position[x] for x in list(number))
        sorted_decoded = sorted(decoded)
        number = positions_to_number[''.join(sorted(decoded))]
        number_string += str(positions_to_number[''.join(sorted(decoded))])
        # print(number)
    # print(int(number_string))
    total_sum += int(number_string)
print(total_sum)
    # print(positions_to_number)
    # print(number_list)
    # print(len(set(number_list)))
    

    # for number in number_list:
    #     print(sorted(number))

    # for aa in ("A", "B")
    # for string in line.split("|")[1].split(" "):
    #     print(string)
    #     if(len(string) in (2, 4, 3, 7)):
    #         print(string, len(string))
    #         unique_count += 1

