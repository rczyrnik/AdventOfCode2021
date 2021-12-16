def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]


# guess: 658
# guess: 545

data = read_data('input4.txt')

grid = []
for line in data:
    grid.append([int(x) for x in line])

for line in grid:
    for number in line:
        print(number, end = ' ')
    print()

# LEVEL 1

# end points: (1, 0) and (0, 1)
# routes: (1,0) and (0,1)
# valuse: 1 and 1
# output: {(1,0): 1, (0,1): 1}

# LEVEL 2
# end points: (2,0), (1, 1), (0, 2)
# routes: (1,0) --> (2,0): 1 + 2 = 3
            # (1,0) --> (1,1) : 1 + 3 = 4
            # (0,1) --> (1,1) : 1 + 3 = 4
            # (0,1) --> (0,2) : 1 + 6 = 7

def do_step(end_points_dict, step):
    end_points = []
    for i in range(step+1):
        x = i
        y = step - i
        if x >= len(grid) or y >= len(grid):
            pass
        else:
            end_points.append([i, step-i])
    # print(end_points)

    for (x,y) in end_points:
        point_value = grid[y][x]
        up = (x-1,y)
        left = (x, y-1)

        if x == 0:
            end_points_dict[(x,y)] = end_points_dict[left] + point_value
        elif y == 0:
            end_points_dict[(x,y)] = end_points_dict[up] + point_value
        else:
            end_points_dict[(x,y)] = min(end_points_dict[left] , end_points_dict[up]) + point_value
    return(end_points_dict)

# # GENERATE END POINTS
end_points_dict = {(0,0):0}
# for step in range(1, len(grid[0])*2):
for step in range(1, 101):
    end_points_dict = do_step(end_points_dict, step)
# for (a, b) in end_points_dict:
#     print(a, b, end_points_dict[(a, b)])






# print(end_points_dict)
# print(grid[99][99])
# do_step(end_points_dict, 100)
# for a in range(100):
#     for b in range(100):
#         print(a, b, end_points_dict[(a, b)])





# print(forend_points_dict)

# print(len(grid), len(grid[0]))
# ()
# end_points_dict = do_step(end_points_dict, 2)
# print(end_points_dict)
    # print(x, y)
    # if x = 0:
    #     end_points_dict.append(())
    # up = (x-1,y)
    # left = (x, y-1)
    # print(up, left)
    