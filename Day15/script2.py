def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def make_grid(data):
    digit_dict = {n:n+1 for n in range(1,9)}
    digit_dict[9] = 1
    grid = []
    for line in data:
        line1 = [int(x) for x in line]
        line2 = [digit_dict[x] for x in line1]
        line3 = [digit_dict[x] for x in line2]
        line4 = [digit_dict[x] for x in line3]
        line5 = [digit_dict[x] for x in line4]
        grid.append(line1+line2+line3+line4+line5)

    for i in range(0, len(grid)*4):
        grid.append([digit_dict[n] for n in grid[i]])
    
    return(grid)

def display_grid(grid):
    for line in grid: 
        for number in line:
            print(number, end=" ")
        print()

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

# /--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--//--/

data = read_data('input2.txt')

grid = make_grid(data)
# display_grid(grid)

# GENERATE END POINTS
end_points_dict = {(0,0):0}

for step in range(1, 1000):
    end_points_dict = do_step(end_points_dict, step)

blank_grid = [[0 for x in range(500)] for y in range(500)]

x = 499
y = 499
while x > 0 and y > 0:
    blank_grid[y][x]= 1
    if end_points_dict[(x-1, y)] < end_points_dict[(x, y-1)]:
        x -= 1
    else:
        y -= 1
display_grid(blank_grid)