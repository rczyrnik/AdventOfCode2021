from  itertools import combinations_with_replacement

def get_new_position(movement, position):
    if position + movement > 10:
        return position + movement - 10
    else:
        return position + movement
frequency_dict = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}


def get_score(roll, position):
    score = 0
    universes = 1
    for movement in roll:
        position = get_new_position(movement, position)
        score += position
        universes *= frequency_dict[movement]
    # print(roll, score, universes)
    return(score, universes)

roll_combinations_1 = [list(x) for x in combinations_with_replacement([3, 4, 5, 6, 7, 8, 9],1)]
roll_combinations_2 = [list(x) for x in combinations_with_replacement([3, 4, 5, 6, 7, 8, 9],1)]

# Player 1 Stuff
initial_1 = 4
winning_universes_1 = 0
non_winning_universes_1 = 0
new_roll_combinations_1 = []

# Player 2 Stuff
initial_2 = 9
winning_universes_2 = 0
non_winning_universes_2 = 0
new_roll_combinations_2 = []

total_winning_1 = 0
total_winning_2 = 0

total_winning_universes_1 = 0
total_non_winning_universes_1 = 0
total_winning_universes_2 = 0
total_non_winning_universes_2 = 0
new_winning_universes_1 = 0
new_non_winning_universes_1 = 0
new_winning_universes_2 = 0
new_non_winning_universes_2 = 0
for i in range(1,20):
    new_winning_universes_1 = 0
    new_non_winning_universes_1 = 0


    new_roll_combinations_1 = []
    new_roll_combinations_2 = []

    for roll in roll_combinations_1:
        score, universes = get_score(roll, initial_1)
        if score > 20:
            new_winning_universes_1 += universes
        else:
            new_non_winning_universes_1 += universes
            for x in range(3,10):
                new_roll_combinations_1.append(roll + [x])

    # total number of winning has to account for all the universes created by the opposing player
        # but only those universes where the opposing player hasn't won
        # hence total_winning_universes_1 = 
    # print(new_non_winning_universes_1 , total_non_winning_universes_2, new_non_winning_universes_1 * total_non_winning_universes_2)
    total_winning_universes_1 = new_winning_universes_1 * max(new_non_winning_universes_2, 1)
    total_non_winning_universes_1 = new_non_winning_universes_1 * max(new_non_winning_universes_2,1)
    total_winning_1 += total_winning_universes_1

    roll_combinations_1 = new_roll_combinations_1.copy()
    print("#1 TURN {}, max_universes {}:\t new_winning {}\t total_winning {}\t new_non_winning {}\t total_non_winning {}".format(
                    i, (27**i) * (27**(i-1)),  new_winning_universes_1, total_winning_universes_1, new_non_winning_universes_1, total_non_winning_universes_1))
    # print("new combinations lenght: ", len(roll_combinations_1))
    # Player 2 Turn 1
    new_winning_universes_2 = 0
    new_non_winning_universes_2 = 0
    for roll in roll_combinations_2:
        score, universes = get_score(roll, initial_2)
        if score > 20:
            new_winning_universes_2 += universes
        else:
            new_non_winning_universes_2 += universes
            for x in range(3,10):
                new_roll_combinations_2.append(roll + [x])
    total_winning_universes_2 = new_winning_universes_2 * new_non_winning_universes_1
    total_non_winning_universes_2 = new_non_winning_universes_2 * new_non_winning_universes_1
    total_winning_2 += total_winning_universes_2

    roll_combinations_2 = new_roll_combinations_2.copy()
    print("#2 TURN {}, max_universes {}: new_winning {}\t total_winning {}\t new_non_winning {}\t total_non_winning {}".format(i, (27**i) * (27**(i)), new_winning_universes_2, total_winning_universes_2, new_non_winning_universes_2, total_non_winning_universes_2))

    print()

# print(new_roll_combinations_1[1:5])

print(max(total_winning_1, total_winning_2))