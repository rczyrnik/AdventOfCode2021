from functions import *

file_name = 'input2a.txt'
decoder = list(read_data(file_name)[0])
binary_dict = {'#':1, '.':0}

file_name = 'input2b.txt'
image = get_image(file_name)




def enhance(image, step):
    padded_image = pad_image(image, step)

    width = len(padded_image[0])
    height = len(padded_image)

    new_image = []
    for y in range(1,height-1):
        new_line = []
        for x in range(1,width-1):
            image_string = padded_image[y-1][x-1:x+2] + padded_image[y][x-1:x+2] + padded_image[y+1][x-1:x+2]
            new_line.append(decoder[get_index(image_string)])
        new_image.append(new_line)
    return(new_image)

step_count = 50
for i in range(step_count):
    image = enhance(image, i+1)

print(count_hexes(image))