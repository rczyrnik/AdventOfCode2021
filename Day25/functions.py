def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def get_seafloor(file_name):
    data = read_data(file_name)
    return([list(line) for line in data])

def make_grid():
    grid = {}
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                grid[tuple([x, y, z])] = 0
    return(grid)

def display_seafloor(seafloor):
    for row in seafloor:
        print(''.join(row))
    print()