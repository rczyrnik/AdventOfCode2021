from functions import *

def h_to_r(burrow, hall_index):
  # print("running h to r")
  # find the shrimp and his room
  shrimp = burrow[4][hall_index]            # a string, A, B, C, D
  correct_room_index = room_dict[shrimp]    # an int, 0, 1, 2, 3
  correct_room = burrow[correct_room_index] # a list or shrimp

  # can the shrimp get to that room?
  room_hall_index = 2 + (2*correct_room_index)
  for x in range(min(room_hall_index, hall_index)+1, max(room_hall_index, hall_index)):
    # print(x)
    if burrow[4][x] != '.': 
      # print("there's another shrimp in the way")
      return(False)

  # are there non-matching shrimp in that room?
  all_shrimp = ['A','B','C','D']
  all_shrimp.remove(shrimp)
  for test_shrimp in all_shrimp:
    if test_shrimp in correct_room:
      # print("There's a problem shrimp in the room")
      return(False)
  # print(all_shrimp)


  # print("Move the shrimp!")
  burrow[4][hall_index] = '.'
  burrow[correct_room_index] = [shrimp] + burrow[correct_room_index]
  # print(burrow[correct_room_index])
  if correct_room_index in burrow[5]: burrow[5].remove(correct_room_index)
  # if burrow == [['A','A','A','A'],['B','B','B','B'],['C','C','C','C'],['D','D','D','D'],['.','.','.','.','.','.','.','.','.','.','.'],[]]:
  #   display_burrow(burrow, level, star)

  # get the cost
  room_x_value = 2 + (2*correct_room_index)
  hall_cost = abs(hall_index - room_x_value)
  room_cost = star+1 - len(burrow[correct_room_index])
  multiplier = energy_dict[shrimp]
  cost = multiplier * (room_cost + hall_cost)
  # print("room cost: {} hall cost: {} total cost: {}".format(room_cost, hall_cost, cost))
  # print(cost)
  burrow[6][0] += cost
  return(burrow)


def r_to_h(burrow, room_index, hall_index):
  # check valid

  # is there a shrimp in the room?
  if len(burrow[room_index]) == 0:
    return(False)
  # are there shrimp in the way
  room_position = 2 + (2*room_index)
  for x in range(min(room_position, hall_index), max(room_position, hall_index)):
    if burrow[4][x] != '.':
      # print("CAN'T PASS THROUGH SHRIMP")
      return(False)
  if burrow[4][hall_index] != '.':
    # print("CAN'T LAND ON SHRIMP")
    return(False)

  # move the shrimp
  shrimp = burrow[room_index].pop(0)
  burrow[4][hall_index] = shrimp
  # display_burrow(burrow, level, 2)

  # get the cost
  room_x_value = 2 + (2*room_index)
  hall_cost = abs(hall_index - room_x_value)
  room_cost = star+2 - len(burrow[room_index])
  multiplier = energy_dict[shrimp]
  cost = multiplier * (room_cost + hall_cost)
  # print(cost)
  burrow[6][0] += cost
  return(burrow)



# each turn, either
# 1. room --> hall
#       one of four rooms, to one of (at most) 7 spaces
#       can't pass through a shrimp
#       can't land on a shrimp
#       can't stop at 2, 4, 6, 8
# 2. hall --> room
#       one of (at most) four shrimp to (at most) 1 room
#       room can't have any other shrimp types

def move_shrimp(burrow, level):
  global min_cost
  global has_sln

  # first go through the hall.
  #    A. if there's a shrimp in that spot, see if the shrimp can move to a room
  #    if there's not a shrimp in that spot, try moving shrimps there

  # A
  for hall_index in [0,1,3,5,7,9,10]:
    if burrow[4][hall_index] != '.':
      new_burrow = [list.copy() for list in burrow]
      new_burrow = h_to_r(new_burrow, hall_index)
      if new_burrow:
        level += 1
        move_shrimp(new_burrow, level)

    # B
    else:
      for room_index in burrow[5]: # later 0,1,2,3
        new_burrow = [list.copy() for list in burrow]
        new_burrow = r_to_h(new_burrow, room_index, hall_index)

        if new_burrow:
          level += 1
          move_shrimp(new_burrow, level)
          level -= 1

  # check if complete:
  if min([len(room) == 2 for room in burrow[:3]]):
    if burrow[6][0] < min_cost: 
      min_cost = burrow[6][0]
      has_sln = True
      print(min_cost)




# --``--``--``--``--``--``--``--``--``--``--``--``--``--``--``--``--``--```



# room1 = ['A', 'A']
# room2 = ['B', 'B']
# room3 = []
# room4 = ['D']
# hall = ['D','C','.','C','.','.','.','.','.','.','.']
# available_rooms = []
# cost = 0
# burrow = [room1, room2, room3, room4, hall, available_rooms, 0]
min_cost = 1000000000
has_sln = False
star = 2 # 2 or 4
level = 0
energy_dict = {'A':1,'B':10,'C':100,'D':1000}
room_dict = {'A':0,'B':1,'C':2,'D':3}
burrow = get_burrow(star)
display_burrow(burrow, level, star)

# total_cost = 0
# level = 0
move_shrimp(burrow, level)
print(min_cost)
print(has_sln)