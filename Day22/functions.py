def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def make_grid():
    grid = {}
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                grid[tuple([x, y, z])] = 0
    return(grid)

def truncate_num(num):
    if num < -50: 
        return(-51)
    elif num > 50: 
        return(51)
    else:
        return(num)

def decode_line(line):
    split_1 = line.split(" ")
    on_off = split_1[0]
    ranges = split_1[1]

    x_y_z = ranges.split(",")

    x1, x2 = [truncate_num(int(n)) for n in x_y_z[0].split("=")[1].split("..")]
    y1, y2 = [truncate_num(int(n)) for n in x_y_z[1].split("=")[1].split("..")]
    z1, z2 = [truncate_num(int(n)) for n in x_y_z[2].split("=")[1].split("..")]

    return(on_off,x1,x2,y1,y2,z1,z2)

def update_grid(grid,on_off,x1,x2,y1,y2,z1,z2):
    if on_off == 'on':
        new_val = 1
    elif on_off == 'off':
        new_val = 0
    else:
        print("irregular value: ", on_off)
        new_val = 2
    for x in range(max(x1,-50),min(x2,50)+1):
        for y in range(max(y1,-50),min(y2,50)+1):
            for z in range(max(z1,-50),min(z2,50)+1):
                grid[(x, y, z)] = new_val
    return(grid)

def count_on(grid):
    on_count = 0
    for key, item in grid.items():
        if item == 1:
            on_count += 1
    return on_count