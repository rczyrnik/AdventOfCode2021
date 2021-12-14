def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def get_folds(raw_folds):
    folds = []
    for fold in raw_folds:
        folds.append(fold.split(" ")[2].split("="))
    return(folds)

def get_dots(raw_dots):
    dots = []
    for dot in raw_dots:
        x, y  =  dot.split(",")
        dots.append([int(x),int(y)])
    return(dots)

def get_grid(dots):
    width = max([dot[0] for dot in dots])+2
    height = max([dot[1] for dot in dots])+2
    grid = []
    for y in range(height): grid.append([0]*width)
    for dot in dots: grid[dot[1]][dot[0]]= 1
    return(grid)

def display_grid(dots):
    grid = get_grid(dots)  
    for row in grid: print(row)

# ----------------------------------------------------------------
raw_dots = read_data("input2a.txt")
raw_folds = read_data("input2b.txt")

folds = get_folds(raw_folds)
dots = get_dots(raw_dots)

grid = get_grid(dots)


def do_fold(dots, direction, position):
    position = int(position)
    new_dots = []
    if direction == "x":
        for dot in dots:
            x = dot[0]
            y = dot[1]
            if x > position:
                new_dots.append([(2*position)-x,y])
            else:
                new_dots.append([x,y])
    elif direction == "y":
        for dot in dots:
            x = dot[0]
            y = dot[1]
            if y > position:
                new_dots.append([x,(2*position)-y])
            else:
                new_dots.append([x,y])
    return(new_dots)     

for fold in folds:
    dots = do_fold(dots,fold[0],fold[1])
display_grid(dots)



# print(raw_dots)
# print(raw_folds)

# xx = 655
# yy = 7
# dots = [pair.split(",") for pair in data]
# # print(dots)

# # my_set = set()

# # print(len(my_set))


# my_set = set()
# for dot in dots:
#     x = int(dot[0])
#     y = int(dot[1])
#     if x < 655:
#         my_set.add(str(x)+","+str(y))
#     else:
#         my_set.add(str((2*655)-x)+","+str(y))

# print(len(my_set))