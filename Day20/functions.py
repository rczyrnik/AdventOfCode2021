def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]


def get_image(file_name):
    raw_image = read_data(file_name)
    return([list(line) for line in raw_image])
 
def display_image(image):
    for line in image:
        print(''.join(line))
    print()

def pad_image(image, step):
    if step%2 == 1:
        char = '.'
    else:
        char = "#"
    step_1 = [ [char,char,char,char,char,char,char,char,char] + line + [char,char,char,char,char,char,char,char,char]  for line in image]
    width = len(step_1[0])
    step_2 = [[char]*width] + [[char]*width] + [[char]*width] + [[char]*width] + [[char]*width] + [[char]*width] \
            + step_1 \
            + [[char]*width] + [[char]*width] + [[char]*width] + [[char]*width] + [[char]*width] + [[char]*width] 
    return(step_2)

def get_index(image_string):
    binary_dict = {'#':1, '.':0}
    number = 0
    place = 0
    for char in image_string[::-1]:
        number += binary_dict[char] * 2**place
        place += 1
    return(number)


def count_hexes(image):
    lit_count = 0
    for line in image:
        for char in line:
            if char == "#": lit_count += 1
    return(lit_count)