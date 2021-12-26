from functions_4 import *

def hall_to_room(burrow, hall_index, room_index):
  # already checked that we have the right room and the room is eligible
  shrimp = burrow[hall_index][0]

  # can the shrimp get to that room?
  for index in range(min(room_index, hall_index)+1, max(room_index, hall_index)):
    # print(x)
    if index%2 == 1 and burrow[index] != []: 
      # print("there's another shrimp in the way")
      return(False)

  # print("Move the shrimp!")
  burrow[hall_index] = []
  burrow[room_index] = [shrimp] + burrow[room_index]

  # get the cost
  hall_cost = abs(hall_index - room_index)
  room_cost = 1 + star - len(burrow[room_index])
  multiplier = energy_dict[shrimp]
  cost = multiplier * (room_cost + hall_cost)
  burrow[12][0] += cost
  return(burrow)


def room_to_hall(burrow, room_index, hall_index):
  # remove from room
  shrimp = burrow[room_index].pop(0)

  # place in hall
  burrow[hall_index] = [shrimp]

  # did we empty the room? remove from the list
  if len(burrow[room_index]) == 0:
    burrow[11].remove(room_index)

  # get the cost
  hall_cost = abs(hall_index - room_index)
  room_cost = (star - len(burrow[room_index]))
  multiplier = energy_dict[shrimp]
  cost = multiplier * (room_cost + hall_cost)
  # print("room cost: {} hall cost: {} total cost: {}".format(room_cost, hall_cost, cost))
  burrow[12][0] += cost
  return(burrow)


def move_shrimp(burrow):
  global min_cost
  global has_sln

  for hall_index in [0,1,3,5,7,9,10]:   # create up to 7 branches with either the "if" statment or the 'else' statement
    # A: there's a shrimp in that spot, see if the shrimp can move to a room
    if burrow[hall_index] != []:        # there's a shrimp there
      shrimp = burrow[hall_index][0]    # get the shrimp type (A, B, C, D)
      room_index = room_dict[shrimp]    # find the right room for this shrimp to go to
      if room_index not in burrow[11]:  # means it's been emptied (and we can move our shrimp there)
        new_burrow = [list.copy() for list in burrow]   # new copy for branch
        new_burrow = hall_to_room(new_burrow, hall_index, room_index) # try to move from hall to room
        if new_burrow:                                      # might not have worked (if another shrimp in the way eg)
          # new_burrow[13].append([room_index, hall_index])   # add to the path
          move_shrimp(new_burrow)                           # go a layer deeper

    # B: there's not a shrimp in that spot, try moving shrimps there
    # 1. Create list of rooms to look in
    else:
      # what rooms have shrimp that can reach this hall spot?
      eligible_rooms = get_eligible_rooms(burrow, hall_index)

      # move to those rooms
      for room_index in eligible_rooms:
        new_burrow = [list.copy() for list in burrow]     # new burrow for new branch
        new_burrow = room_to_hall(new_burrow, room_index, hall_index) # try to move the shrimp
        # new_burrow[13].append([room_index, hall_index])   # add this step to the path
        move_shrimp(new_burrow)                           # go a layer deeper


  # check if complete:
  if min([len(burrow[i]) == star for i in [2, 4, 6, 8]]):
    # print(burrow[13])
    has_sln = True
    if burrow[12][0] < min_cost: 
      min_cost = burrow[12][0]
      has_sln = True
      print(min_cost, burrow[13])




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
star = 4 # 2 or 4
level = 0
energy_dict = {'A':1,'B':10,'C':100,'D':1000}
room_dict = {'A':2,'B':4,'C':6,'D':8}
burrow = get_burrow(star)
# display_burrow(burrow, level, star)

total_cost = 0
level = 0
move_shrimp(burrow)
print(min_cost)
print(has_sln)
