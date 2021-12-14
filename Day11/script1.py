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
    print()

def add_one_to_octopi(grid):
    for i in range(12):
        for j in range(12):
            grid[i][j] += 1

def round_of_flashes(grid, flash_list):
    flag = False
    for i in range(1, 11):
        for j in range(1, 11):
            if grid[i][j] > 9:
                if [i,j] not in flash_list:
                    flag = True
                    flash_list.append([i,j])
                    grid[i+1][j] += 1
                    grid[i-1][j] += 1
                    grid[i][j+1] += 1
                    grid[i][j-1] += 1  
                    grid[i+1][j+1] += 1
                    grid[i+1][j-1] += 1
                    grid[i-1][j+1] += 1
                    grid[i-1][j-1] += 1                               
    return flag

def reset_flashed_to_zero(grid, flash_list):
    for coordinate in flash_list:
        grid[coordinate[0]][coordinate[1]] = 0
    flash_list = []

flash_list = []
flash_count = 0
grid = create_grid(read_data("input2.txt"))
display_grid(grid)
first_total_flash = 0

while first_total_flash = 0:
    flash_list = []
    add_one_to_octopi(grid)

    flag = True
    while flag:
        flag = round_of_flashes(grid, flash_list)
    flash_count += len(flash_list)

    if first_total_flash == 0 and len(flash_list) == 100:
        first_total_flash = i+1

    reset_flashed_to_zero(grid, flash_list)
 

print(flash_count, first_total_flash)
# print()
# display_grid(grid)