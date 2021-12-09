# ~~ - ~~ - imports - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 

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
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = " ")
        print()

# ~~ - ~~ - program - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - ~~ - 
raw_input = read_data("input2.csv")

grid = create_grid(raw_input)

my_sum = 0
for i in range(1,len(grid)):
    for j in range(1,len(grid[0])):
       if grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i+1][j] and grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i][j+1]: 
            my_sum += (grid[i][j] + 1)

print(my_sum)