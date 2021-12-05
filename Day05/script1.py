def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

data = read_data('data1b.csv')

x1_list = []
x2_list = []
y1_list = []
y2_list = []

# max_x = 10
# max_y = 10
max_x = 1000
max_y = 1000

grid = []

for i in range(max_x):
    grid.append([0]*max_y)

def display_grid():
    for y in range(max_y):
        for x in range(max_x):
            print(grid[x][y], end = "")
        print()

def update_grid_y(x1, y1, y2):
    if y2 > y1:
        for y in range(y1, y2+1):
            grid[x1][y] += 1
    elif y1 > y2:
        for y in range(y2, y1+1):
            grid[x1][y] += 1        

def update_grid_x(y1, x1, x2):
    if x2 > x1:
        for x in range(x1, x2+1):
            grid[x][y1] += 1
    elif x1 > x2:
        for x in range(x2, x1+1):
            grid[x][y1] += 1

for i in range(len(data)):
    x1, y1 = data[i].split()[0].split(',')
    x2, y2 = data[i].split()[2].split(',')
    if x1 == x2:
        update_grid_y(int(x1), int(y1), int(y2))
    elif y1 == y2:
        update_grid_x(int(y1), int(x1), int(x2))

danger_zones = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] > 1: danger_zones += 1

print(danger_zones)



