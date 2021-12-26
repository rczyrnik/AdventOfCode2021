
frequency_dict = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}



def get_new_position(movement, position):
    if position + movement > 10:
        return position + movement - 10
    else:
        return position + movement




# def one_turn(p1_universes, p1_position, p1_score, p2_universes, p2_position, p2_score):
#     p1_new_wins = 0
#     p1_new_non_wins = 0
#     p1_new_win_universes = 0
#     p1_new_win_universes = 0

#     p2_new_wins = 0
#     p2_new_non_wins = 0
#     p2_new_win_universes = 0
#     p2_new_win_universes = 0
   
#     position = 4
#     p1_score = 0
def one_turn(position, score):

    # PLAYER 1'S SCORE
    wins1 = 0
    non_wins1 = 0
    for movement in range(3, 10):
        new_score = score
        new_position = get_new_position(movement, position)
        new_score += new_position
        print("new position {}\t new score {}".format(new_position, new_score))
        if new_score > 20:
            new_wins += frequency_dict[movement]
        else:
            new_non_wins += frequency_dict[movement]

            # PLAYER 2'S TURN
    print("\n", new_wins, new_non_wins)

one_turn(4, 0)


# p0 = 4
# s0 = 0
# wins = 0
# non_wins = 0
# for m1 in range(3, 10):
#     p1 = get_new_position(m1, p0)
#     s1 = s0 + p1
#     for m2 in range(3, 10):
#         p2 = get_new_position(m2, p1)
#         s2 = s1 + p2
#         for m3 in range(3, 10):
#             p3 = get_new_position(m3, p2)
#             s3 = s2 + p3
#             print("movements: {}\t{}\t{}\tpositions: {}\t{}\t{}\tscore: {}\t winning? {}".format(m1,m2,m3,p1,p2,p3,s3,s3>20))
#             if s3 > 20:
#                 wins += frequency_dict[m1]*frequency_dict[m2]*frequency_dict[m3]
#             else: 
#                 non_wins += frequency_dict[m1]*frequency_dict[m2]*frequency_dict[m3]
# print(wins, non_wins)
