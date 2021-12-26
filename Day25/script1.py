from functions import *

file_name = 'input0.txt'
seafloor = get_seafloor(file_name)
# display_seafloor(seafloor)


# add buffer to top and left
# print()


width = len(seafloor[0])
height = len(seafloor)

# print("width: {}, height: {}".format(width, height))
def single_step(seafloor):

    temp_seafloor = [[list[-1]] + list + [list[0]] for list in seafloor]
    temp_seafloor = [temp_seafloor[-1].copy()] + temp_seafloor + [temp_seafloor[0].copy()]
    new_seafloor = [list.copy() for list in temp_seafloor]
    # display_seafloor(temp_seafloor)


    # east ward
    x_flag = False
    for y in range(height+2):
        for x in range(width, -1, -1):
            if temp_seafloor[y][x] == ">" and temp_seafloor[y][x+1] == '.':
                new_seafloor[y][x] = '.'
                new_seafloor[y][x+1] = ">"
                x_flag = True
    # display_seafloor(temp_seafloor)

    temp_seafloor = [list.copy() for list in new_seafloor]
 
    # print(len(temp_seafloor))
    # south ward
    y_flag = False
    for y in range(height, -1, -1):
        for x in range(width+2):
            if temp_seafloor[y][x] == "v" and temp_seafloor[y+1][x] == '.':
                new_seafloor[y][x] = '.'
                new_seafloor[y+1][x] = "v"
                y_flag = True
                # print("x: {}\ty: {}".format(x, y))
                # display_seafloor(temp_seafloor)
                # print()
    # display_seafloor(temp_seafloor)
    # print()    
    return([row[1:-1] for row in new_seafloor[1:-1]], x_flag or y_flag)

flag = True
i = 1
while flag:
    seafloor, flag = single_step(seafloor)
    # print(i, flag)
    # display_seafloor(seafloor)
    # print()
    i += 1
print(i-1)
# display_seafloor(seafloor)