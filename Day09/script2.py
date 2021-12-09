# ~~ - ~~ - imports - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
from collections import Counter

# ~~ - ~~ - functions - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def create_grid(raw_input):
   return ( [[10]*(len(raw_input[0])+2)] \
            + [[10] + [int(y) for y in list(x)] + [10] for x in raw_input] \
            + [[10]*(len(raw_input[0])+2)] )

def display_grid(grid):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            print(grid[i][j], end = " ")
        print()

def identify_basins():
    basin_num = -1
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] < grid[i-1][j] \
                    and grid[i][j] < grid[i+1][j] \
                    and grid[i][j] < grid[i][j-1]  \
                    and grid[i][j] < grid[i][j+1]: 
                    grid[i][j] = basin_num
                    basin_num -= 1

def run_update(grid):
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] == 9 or grid[i][j] == 10: pass
            elif grid[i-1][j] < 0: grid[i][j] = grid[i-1][j]
            elif grid[i+1][j] < 0: grid[i][j] = grid[i+1][j]
            elif grid[i][j-1] < 0: grid[i][j] = grid[i][j-1]
            elif grid[i][j+1] < 0: grid[i][j] = grid[i][j+1]

def check_grid(grid):
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] < 9 and grid[i][j] > 0: return(True)
    else: return(False)

# ~~ - ~~ - program - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 

# read data
raw_input = read_data("input2.csv")
grid = create_grid(raw_input)

# identify basins
identify_basins()

# fill in basins
while check_grid(grid):
    run_update(grid)

# get the sizes of the basins
master_list = []
for item in grid: master_list += item

basin_size_dict = Counter(master_list)
basin_size_dict.pop(9)
basin_size_dict.pop(10)

# find the solution
basin_sizes = sorted(basin_size_dict.values())
print(basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])
