# def read_data(file_name):
# 	file = open(file_name, 'r')
# 	raw_lines = file.readlines()
# 	file.close()
# 	return [line.strip() for line in raw_lines]

# 


def get_burrow(star):
  if star == 4:
    room1 = ['A', 'D', 'D', 'C']
    room2 = ['D', 'C', 'B', 'C']
    room3 = ['A', 'B', 'A', 'D']
    room4 = ['B', 'A', 'C', 'B']
  if star == 2:
    room1 = ['A', 'C']
    room2 = ['D', 'C']
    room3 = ['A', 'D']
    room4 = ['B', 'B']
  hall = ['.','.','.','.','.','.','.','.','.','.','.']
  available_rooms = [0,1,2,3]
  total_cost = [0]
  return [room1, room2, room3, room4, hall, available_rooms, total_cost]

def display_burrow(burrow, depth, star):
  depth_space = ' '*depth
  room1, room2, room3, room4, hall, _, _ = burrow.copy()

  #  pad to full length for display
  room1 = ['.'] * (star - len(room1)) + room1
  room2 = ['.'] * (star - len(room2)) + room2
  room3 = ['.'] * (star - len(room3)) + room3
  room4 = ['.'] * (star - len(room4)) + room4
  print(depth_space, '  0 1 2 3 4 5 6 7 8 9 10 ')
  print(depth_space, '#########################')

  # hall
  print(depth_space, '# ', end = '')
  for square in hall: print(square[0], end = ' ')
  print('#')

  #rooms
  print(depth_space, '##### {} # {} # {} # {} #####'.format(room1[0][0], room2[0][0], room3[0][0], room4[0][0]))
  for i in range(1,star): print(depth_space,'    # {} # {} # {} # {} #  '.format(room1[i][0], room2[i][0], room3[i][0], room4[i][0]))
  print(depth_space,'    #################  ')
  print(depth_space,'      0   1   2   3    ')

  print()
  print()







# def display_burrow_old(rooms, hall, depth):
#   depth_space = ' '*depth
#   room1, room2, room3, room4 = rooms

#     #   pad to full length for display
#   room1 = ['..'] * (4 - len(room1)) + room1
#   room2 = ['..'] * (4 - len(room2)) + room2
#   room3 = ['..'] * (4 - len(room3)) + room3
#   room4 = ['..'] * (4 - len(room4)) + room4

#   print(depth_space, '  0 1 2 3 4 5 6 7 8 9 10 ')
#   print(depth_space, '#########################')

#   # hall
#   print(depth_space, '# ', end = '')
#   for square in hall:
#     print(square[0], end = ' ')
#   print('#')

#   print(depth_space, '##### {} # {} # {} # {} #####'.format(room1[0][0], room2[0][0], room3[0][0], room4[0][0]))
#   #rooms
#   for i in range(1,4):
#     print(depth_space,'    # {} # {} # {} # {} #  '.format(room1[i][0], room2[i][0], room3[i][0], room4[i][0]))

#   print(depth_space,'    #################  ')
#   print(depth_space,'      0   1   2   3    ')

#   print()
#   print()



# def display_burrow_same_level(rooms, hall):
#   room1, room2, room3, room4 = rooms

#     #   pad to full length for display
#   room1 = ['..'] * (4 - len(room1)) + room1
#   room2 = ['..'] * (4 - len(room2)) + room2
#   room3 = ['..'] * (4 - len(room3)) + room3
#   room4 = ['..'] * (4 - len(room4)) + room4

#   print('  0 1 2 3 4 5 6 7 8 9 10 ')
#   print('#########################')

#   # hall
#   print('# ', end = '')
#   for square in hall:
#     print(square[0], end = ' ')
#   print('#')

#   print('##### {} # {} # {} # {} #####'.format(room1[0][0], room2[0][0], room3[0][0], room4[0][0]))
#   #rooms
#   for i in range(1,4):
#     print('    # {} # {} # {} # {} #  '.format(room1[i][0], room2[i][0], room3[i][0], room4[i][0]))

#   print('    #################  ')
#   print('      0   1   2   3    ')

#   print()
#   print()


# def display_burrow_double(rooms, hall):
#   room1, room2, room3, room4 = rooms
#     #   pad to full lenght for display
#   room1 = ['..'] * (4 - len(room1)) + room1
#   room2 = ['..'] * (4 - len(room2)) + room2
#   room3 = ['..'] * (4 - len(room3)) + room3
#   room4 = ['..'] * (4 - len(room4)) + room4
#   print('##0####1####2####3####4####5####6####7####8####9####10##')
#   # hall
#   print('# ', end = '')
#   for square in hall:
#     print(square, end = ' # ')
#   print()
#   print('########### {} ###### {} ###### {} ###### {} ###########'.format(room1[0], room2[0], room3[0], room4[0]))
#   #rooms
#   for i in range(1,4):
#     print('          # {} ###### {} ###### {} ###### {} #  '.format(room1[i], room2[i], room3[i], room4[i]))

#   print('          ## 0 ###### 1 ######## 2 ###### 3 ##  ')
#   print()
#   print()











#   print()
#   print('####################################################################')
#   # hall
#   print('## ', end = '')
#   for square in hall:
#     print(square, end = ' ## ')
#   print()
#   print('############## {} ######## {} ######## {} ######## {} ##############'.format(room1[0], room2[0], room3[0], room4[0]))
#   #rooms
#   for i in range(1,4):
#     print('            ## {} ######## {} ######## {} ######## {} ##  '.format(room1[i], room2[i], room3[i], room4[i]))

#   print('            ############################################  ')
#   print()
#   print()