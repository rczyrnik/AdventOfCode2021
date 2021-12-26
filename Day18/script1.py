# n = [1,2]
# n = [[1,2],3]
# n = [9,[8,7]]
# n = [[1,9],[8,5]]
# n = [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
# n = [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
# n = [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]



 #--> [[[[0,9],2],3],4]
# n = [7,[6,[5,[4,[3,2]]]]] --> [7,[6,[5,[7,0]]]]
# n = [[6,[5,[4,[3,2]]]],1] --> [[6,[5,[7,0]]],3]
# n = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] --> [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
# n = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] --> [[3,[2,[8,0]]],[9,[5,[7,0]]]]

# print(len(n))

def expand(n, depth, numbers):
    global max_depth
    global count
    global n0
    if isinstance(n, int):
        # print(' '*depth, n)
        numbers[tuple((count,depth))] = n
        count += 1
    else:
        depth += 1
        max_depth += 1
        for m in n:
            expand(m, depth, numbers)


def display_grid(grid):

    for line in grid:
        for char in line:
            print(char, end = '')
        print()
    print()

def create_grid(count, max_depth):
    print("count: {}, max_depth: {}".format(count, max_depth))
    grid = []
    for x in range(count):
        grid.append(["·"]*max_depth)
    return(grid)

def fill_grid(grid, numbers):
    for (count, depth), number in numbers.items():
        grid[count][depth] = number
    return(grid)

def explode(grid):
    l = 0
    change_flag = False
    zero_line = ['·', '·', '·',  0, '·']
    # cycle through each row of the grid
    while l < len(grid):
 
        # find first val at depth 4
        if isinstance(grid[l][4],int):
            change_flag = True
            # EXPLODE LEFT

            #if first number
            if l == 0:
                # print("l-a")
                grid[l] = zero_line
                l += 1
            
            # if not first number, and there's a number right behind
            elif isinstance(grid[l-1][3], int):
                # print("l-b")
                grid[l-1][3] += grid[l][4]
                grid.pop(l)


            # if not first number, and the left number is a few levels back
            else:
                # print("l-c")
                # change the numger
                for i in range(len(grid[l-1])):
                    if isinstance(grid[l-1][i], int):
                        grid[l-1][i] += grid[l][4]
                # add the zero
                grid[l] = zero_line
                l += 1
            # print("after left, l = {}, len_grid = {}".format(l, len(grid)))
            # display_grid(grid)



            # EXPLODE RIGHT
            #if last number
            if l == len(grid)-1:
                # print("r-a")
                grid[l] = zero_line
            
            # if not first number, and there's a number right ahead
            elif isinstance(grid[l+1][3], int):
                # print("r-b")
                grid[l+1][3] += grid[l][4]
                grid.pop(l)

            # if not first number, and the left number is a few levels back
            else:
                # print("r-c")
                # change the numger
                for i in range(len(grid[l+1])):
                    if isinstance(grid[l+1][i], int):
                        grid[l+1][i] += grid[l][4]

                # add the zero
                grid[l] = zero_line

            # print("after right, l = {}, len_grid = {}".format(l, len(grid)))
            # display_grid(grid)

            #issue with no fringe?        
            l = len(grid)
        l += 1
    return(grid, change_flag)

def split(grid):
    l = 0
    change_flag = False
    while l < len(grid):
        i = 0
        while i < 5:
        # for i in range(5):
            if isinstance(grid[l][i], int) and grid[l][i] > 9:
                left_list = [['·', '·', '·', '·', '·']]
                right_list = [['·', '·', '·', '·', '·']]
                left_num = grid[l][i] // 2
                right_num = grid[l][i] - left_num
                left_list[0][i+1] = left_num
                right_list[0][i+1] = right_num
                # print(left_num, right_num)
                grid = grid[:l] + left_list +  right_list + grid[l+1:] 
                l = len(grid)
                i = 6
                change_flag = True
            i += 1
        l += 1
    return(grid, change_flag)

if __name__ == "__main__":
    n = [[[[[9,8],1],2],3],4] #/--> [[[[0,9],2],3],4]
    n = [7,[6,[5,[4,[3,2]]]]] #--> [7,[6,[5,[7,0]]]]
    n = [[6,[5,[4,[3,2]]]],1] #--> [[6,[5,[7,0]]],3]
    n = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] #--> [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
    n = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] #--> [[3,[2,[8,0]]],[9,[5,[7,0]]]]
    n = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    # n = [[[[0,7],4],[15,[0,13]]],[1,1]]
    max_depth = 0
    count = 0
    depth = -1
    numbers = {}
 
    expand(n, depth, numbers)
    grid = create_grid(count, 5)

    
    grid = fill_grid(grid,numbers)
    # print("initial grid")
    # display_grid(grid)

    # explode(grid)
    # display_grid(grid)
    # explode(grid)
print("initial")
display_grid(grid)

big_flag = True
while big_flag:
    grid, change_flag1 = explode(grid)
    display_grid(grid)
    grid, change_flag2 = split(grid)
    display_grid(grid)
    big_flag = change_flag1 or change_flag2

