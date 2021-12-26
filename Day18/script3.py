
def get_char_list(raw_string):
    char_list = []
    integers = [str(x) for x in range(10)]
    for char in raw_string:
        if char in integers:
            char_list.append(int(char))
        else:
            char_list.append(char)
    return(char_list)

def has_int(my_list):
    for x in my_list:
        if isinstance(x,int):
            return(True)
    return(False)

def find_cursor(cursor, char_list):
    display(char_list)
    print('000000000011111111112222222222333333333344444444445555555555')
    print('012345678901234567890123456789012345678901234567890123456789')
    print("cursor: ", cursor)

def explode(char_list):
    flag = False
    depth = 0
    cursor = 0
    while cursor < len(char_list):

        if char_list[cursor] == "[": depth += 1
        if char_list[cursor] == "]": depth -= 1

        if depth == 5: # happens at last [
            # find_cursor(cursor, char_list)
            flag = True
            # EXPLODE LEFT
            this_char = char_list[cursor]
            while not isinstance(this_char, int):
                cursor += 1  # to get to first num
                this_char = char_list[cursor]

            # case 1: there's a number to the left, doesn't need to add a 0
            if isinstance(char_list[cursor-3], int):
                # print(type(char_list[cursor-3]),type(char_list[cursor]) , type(char_list[cursor-3] + char_list[cursor]))
                # print('gotcha')
                char_list[cursor-3] += char_list[cursor]
                # display(char_list)
                # char_list[cursor-3] += char_list[cursor]

                char_list.pop(cursor-2) # remove second number
                char_list.pop(cursor-2) # remove ]
                char_list.pop(cursor-2) # remove ,
                cursor -= 1 # put cursor on second letter
                # print("x")


            # case 2: there's a number to the left, needs to add a 0
            elif has_int(char_list[:cursor]):
                char = '.'
                j = -1
                while not isinstance(char,int):
                    j -= 1
                    char = char_list[cursor+j] 
                char_list[cursor+j] += char_list[cursor]  # add exploded value to next left value
                char_list.pop(cursor-1) # remove [
                char_list.pop(cursor-1) # remove first number
                char_list[cursor-1] = 0 # remove ,
                # cursor -= 1 # put cursor on second char
                # print(char_list[i])

            # add a zero one level lower
            else:
                # print("a ", end = '')
                # display(char_list)
                char_list.pop(cursor-1)  # remove the most recemnt [
                # print("b ", end = '')
                # display(char_list)
                char_list[cursor-1] = 0  # replace the number with 0
                # print("c ", end = '')
                # display(char_list)
                char_list.pop(cursor)

            # EXPLODE RIGHT
            # assumes cursor is on second number
            # i += 1  # to get second num

            this_char = char_list[cursor]
            while not isinstance(this_char, int):
                cursor += 1  # to get to first num
                this_char = char_list[cursor]
            # print(this_char)
            # print(char_list[cursor])
            # find_cursor(cursor, char_list)

            # case 0: there's a number at the same level to the right
            if char_list[cursor+1:cursor+4] == [']', ',', '['] and isinstance(char_list[cursor+4], int):
                # print("gotcha")
                char_list[cursor+4] += char_list[cursor]
                char_list.pop(cursor) # remove second number
                char_list.pop(cursor) # remove ]

            # case 0: there's a number at the same level to the right
            # if isinstance(char_list[cursor+4], int):
            #     print("gotcha")
            #     char_list[cursor+4] += char_list[cursor]
            #     char_list.pop(cursor) # remove second number
            #     char_list.pop(cursor) # remove ]


            # case 1: there's a number right next door, don't need 0
            elif isinstance(char_list[cursor+3], int):
                #####
                # print(type(char_list[cursor-3]),type(char_list[cursor]) , type(char_list[cursor-3] + char_list[cursor]))

                char_list[cursor+3] += char_list[cursor]
                char_list.pop(cursor) # remove second number
                char_list.pop(cursor) # remove ]
                # char_list.pop(cursor) # remove ,

            # case 2: there's a higher number but farther away
            #         need to add a "0"
            elif has_int(char_list[cursor+4:]):

                char = '.'
                j = 0
                while not isinstance(char,int):
                    j += 1
                    char = char_list[cursor+1+j] 
                char_list[cursor+1+j] += char_list[cursor] # add value to other number
                char_list[cursor] = 0
                char_list.pop(cursor+1) # remove ]
                # char_list.pop(cursor+1) # remove ,

            # add a zero one level lower
            else:
                char_list[cursor] = 0
                char_list.pop(cursor+1)

            # only once per explode
            cursor = len(char_list)
        cursor += 1
    return(char_list, flag)

def get_char_string(char_list):
    return(''.join([str(x) for x in char_list]))

def run_tests_explode():
    test1 = ["[[[[[9,8],1],2],3],4]",'[[[[0,9],2],3],4]']   # c, a
    test2 = ['[7,[6,[5,[4,[3,2]]]]]','[7,[6,[5,[7,0]]]]']   # a, c
    test3 = ['[[6,[5,[4,[3,2]]]],1]','[[6,[5,[7,0]]],3]']   # c, b
    test4 = ['[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]']  # a, c
    test5 = ['[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[7,0]]]]'] # a, c
    test6 = ['[1,[[[[2,3],4],5],6]]', '[3,[[[0,7],5],6]]']
    test7 = ['[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,0]],[[6,6],[8,[[5,6],8]]]]]', '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,0]],[[6,6],[13,[0,14]]]]]']
    test8 = ['[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[6,[7,[7,7]]]]]]','[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[6,[14,0]]]]]']
    test9 = ['[[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]],[7,[5,[[3,8],[1,4]]]]]','[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]']
    tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9]
    for test in tests:
        test_output = get_char_string(explode(get_char_list(test[0]))[0])
        print("\n{}\n         input: {}\n     my output: {}\n  right output: {}".format(test_output == test[1], test[0], test_output, test[1]))

def split(char_list):
    flag = False
    cursor = 0
    while cursor < len(char_list):
        if isinstance(char_list[cursor],int) and char_list[cursor] > 9:
            flag = True
            left_num = char_list[cursor] // 2
            right_num = char_list[cursor] - left_num
            # 15 --> [, l, ,, r, ]
            char_list[cursor] = '['
            char_list.insert(cursor+1, left_num)
            char_list.insert(cursor+2, ',')
            char_list.insert(cursor+3, right_num)
            char_list.insert(cursor+4, ']')

            # print('yay!', left_num, right_num)
            cursor = len(char_list)
        cursor += 1
    return(char_list, flag)

def reduce(char_list):
    big_flag = True
    # print("\ninitial:")
    # display(char_list)
    while big_flag:
        char_list, change_flag1 = explode(char_list)
        # print("\nexploded:")
        # display(char_list)
        if not change_flag1:
            char_list, change_flag2 = split(char_list)
            # print("\nsplit:")
            # display(char_list)
        big_flag = change_flag1 or change_flag2
    return(char_list)

def display(char_list):
    print(get_char_string(char_list))

def add(a, b):
    return(['[']+a+[',']+b+[']'])

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

# --~~//--~~//--~~//--~~//--~~//--~~//--~~//--~~//--~~//--~~//--~~//--~~//--~~//
# run_tests_explode()


file_name = 'input0.txt'
data = [get_char_list(line) for line in read_data(file_name)]

final_list = data[0]
for i in range(1,len(data)):
    list_concat = add(final_list, data[i])
    final_list = reduce(add(final_list, data[i]))
display(final_list)

# char_list = get_char_list('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
# char_list = get_char_list('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
# magnitude1 = ['[[1,2],[[3,4],5]]', 143]
# magnitude1 = ['[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384]
# magnitude1 = ['[[[[1,1],[2,2]],[3,3]],[4,4]]', 445]
# magnitude1 = ['[[[[3,0],[5,3]],[4,4]],[5,5]]', 791]
# magnitude1 = ['[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137]
# magnitude1 = ['[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488]

def magnitude_step(char_list):
    i = 1
    while i < len(char_list):
        if isinstance(char_list[i], int) and char_list[i+1] == ',' and isinstance(char_list[i+2], int):
            char_list[i] = 3*char_list[i] + 2*char_list[i+2]
            char_list.pop(i+1) # remove comma
            char_list.pop(i+1) # remove second number
            char_list.pop(i+1) # remove closing ]
            char_list.pop(i-1) # remove closing ]
        i += 1
    # display(char_list)
    return(char_list)

while len(final_list)>1:
    final_list = magnitude_step(final_list)
print(final_list)
# run_tests()
# display(final_list)
# print('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')





















# steps = ['',
#         '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]', 
#         '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]',
#         '[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]',
#         '[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]',
#         '[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]',
#         '[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]',
#         '[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]',
#         '[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]',
#         '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
#         ]
# my_input = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[6,[7,[7,7]]]]]]'
# my_output = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[13,[07]]]]]]'
# right_output = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[6,[14,0]]]]]'


# initial = get_char_list(my_input)
# output, _ = explode(get_char_list(initial))
# display(output)

# initial9 = '[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[9,[5,5]],20],[8,[9,0]]]]'
# wrong_output = '[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[14,],25],[8,[9,0]]]]'
# right_output = '[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[14,0],25],[8,[9,0]]]]'

# output, _ = explode(get_char_list(initial9))
# display(output)
# test9 = ['[[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]],[7,[5,[[3,8],[1,4]]]]]','[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]']

# input9 = get_char_list(test9[0])
# display(input9)
# display(reduce(input9))


# # run_tests_explode()

# test = ['[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[6,[7,[7,7]]]]]]','[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[5,6]],[[0,6],[6,[14,0]]]]]']
# initial = get_char_list(test[0])
# final = test[1]

# new, _ = explode(initial)
# display(new)

# # [
#     [
#         [
#             [4,0
#             ],
#             [5,4
#             ]
#         ],
#         [   [7,7
#             ],
#             [6,0
#             ]
#         ]
#     ],
#     [   [   [6,6
#             ],
#             [5,0
#             ]
#         ],
#         [   [6,6
#             ],
#             [8,
#                 [   [5,6
#                     ]
#                 ,8
#                 ]
#             ]
#         ]
#     ]
# ]

# /**


# test = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
# char_list = get_char_list(test)
# split1 = ['[', '[', '[', '[', 0, ',', 7, ']', ',', 4, ']', ',', '[', 15, ',', '[', 0, ',', 13, ']', ']', ']', ',', '[', 1, ',', 1, ']', ']']


# print(explode(get_char_list('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]')))

# a = get_char_list('[[[[4,3],4],4],[7,[[8,4],9]]]')
# b = get_char_list('[1,1]')

# print(a)
# print(b)

# # print(['a']+['b'])
# display(add(a, b))
# display(reduce(add(a, b)))

# my_input = ['[', '[', '[', '[', '[', 1, ',', 1, ']', ',', '[', 2, ',', 2, ']', ']', ',', '[', 3, ',', 3, ']', ']', ',', '[', 4, ',', 4, ']', ']', ',', '[', 5, ',', 5, ']', ']']

# display(my_input)
# my_input, _ = explode(my_input)

# display(my_input)
# # display(my_input)
# display(reduce(my_input))

# initial: [[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]
# explode 1: [[[[0,[3,2]],[3,3]],[4,4]],[5,5]]
# explode 2:[[[[3,0],[5,3]],[4,4]],[5,5]]


# test_6 = ['[1,[[[[2,3],4],5],6]]', '[3,[[[0,7],5],6]]']
# print(test_6[0][::-1])

# ['[1,[[[[2,3],4],5],6]]', '[3,[[[0,7],5],6]]']
# my_input = '[[[[[9,8],1],2],3],4]'
# # # my_input = '[7,[6,[5,[4,[3,2]]]]]'
# # my_input = '[[6,[5,[4,[3,2]]]],1]'
# print(my_input)
# print(get_char_string(explode(get_char_list(my_input))))


# char_string = ''.join([str(x) for x in explode(char_list)])
# print("[[[[0,9],2],3],4]"''.join([str(x) for x in explode(char_list)]))