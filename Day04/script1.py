import math

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def check_board(board, winners):
    for winner in winners:
        my_sum = 0
        for b, w in zip(board, winner):
            my_sum += b*w
        if my_sum == 5:
            return True
    return False


# get list of winning boards
winners = [[int(y) for y in list(x)] for x in read_data('winning_strings.csv')]

# get list of numbers
numbers = [int(i) for i in read_data('data2a.csv')[0].split(",")]

# create boards and scoreboards
boards_raw = read_data('data2b.csv')
boards = []
scoreboards = []
this_board = []
for i in range (len(boards_raw)):
    if boards_raw[i] == '':
        boards.append(this_board)
        scoreboards.append([0]*25)
        this_board = []
    else:
        this_board += [int(x) for x in boards_raw[i].split()]
boards.append(this_board)
scoreboards.append([0]*25)


# play the game
def play_game():
    for number in numbers:
        # find the number (if exists) in each board
        for board, scoreboard in zip(boards, scoreboards):
            if number in board: scoreboard[board.index(number)] = 1
            if check_board(scoreboard, winners): return(board, scoreboard, number)

board, scoreboard, number = play_game()
# print(board, scoreboard, number)
my_sum = 0
for b, w in zip(board, scoreboard):
    my_sum += b*(1-w)
print(my_sum*number)
