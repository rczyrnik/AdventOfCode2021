from functions import *
#############
#...........#
###A#D#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #C#C#D#B#
  #########


def rh(room_index, hall_index):
  global total_cost
  # room_index -= 1
  # hall_index -= 1
  shrimp = burrow[room_index].pop(0)
  burrow[4][hall_index] = shrimp

  room_x_value = 2 + (2*room_index)
  hall_cost = abs(hall_index - room_x_value)
  room_cost = 4 - len(burrow[room_index])
  multiplier = energy_dict[shrimp[0]]
  cost = multiplier*(room_cost + hall_cost)
  total_cost += cost
  display(cost)

def hr(hall_index, room_index):
  global total_cost
  # room_index -= 1
  # hall_index -= 1
  shrimp = burrow[4][hall_index]
  burrow[4][hall_index] = '..'
  burrow[room_index] = [shrimp] + burrow[room_index]

  room_x_value = 2 + (2*room_index)
  hall_cost = abs(hall_index - room_x_value)
  room_cost = 4 - len(burrow[room_index])
  multiplier = energy_dict[shrimp[0]]
  cost = multiplier*(room_cost + hall_cost)
  total_cost += cost+1
  display(cost+1)


def display(cost):
  print('',end = '')

  print("cost:",cost, "   total cost:", total_cost)
  display_burrow(burrow, 0, 4)

def rr(a, b, c):
  rh(a,c)
  hr(c,b)

# ~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-~`-


energy_dict = {'A':1,'B':10,'C':100,'D':1000}
room_dict = {'A':0,'B':1,'C':2,'D':3}
burrow = get_burrow(4)
burrow_0 = get_burrow(4)

print('start:')
display_burrow(burrow, 0, 4)
total_cost = 0

# rh(0,0)
# rh(1,10)
# rh(1,1)
# rh(1,5)
# rh(1,3)

# hr(5,1)
# rr(3, 1,5)



# rh(3,0)
# rh(3,10)
# rh(3,9)
# rh(3,1)

# rr(1,3,5)

# rh(1,7)
# rh(1,3)
# rh(1,5)
# hr(3,1)
# hr(1,1)
# hr(0,1)

display_burrow(burrow_0, 0, 4)
# rh(1,10)
# rh(1,0)
# rh(1,3)
# rh(1,1)

# hr(3,1)
# rr(3,1,5)

# rh(3,9)
# rh(3,3)
# rr(3,1,5)








# empty 1 first

# rh(0,10)
# rh(0,9)
# rh(0,7)
# rh(0,0)
# rr(2,0,5)


# rh(0,0)
# rh(0,10)
# rh(0,9)
# rh(0,7)
# rr(2, 0, 5)
# hr(0,0)

# rh(2,0)
# rr(2,0,5)


# rh(2,1)
# hr(7,2)

# rh(1,3)
# rr(1,2,5)
# rh(1,7)
# rr(1,2,5)

# hr(7,1)
# rr(3,1,5)

# rh(2,0)
# rh(2,1)
# rh(2,10)
# rh(2,9)







# # empty B first
# rh(1,0)
# rh(1,1)
# rh(1,3)
# rh(1,10)

# hr(3,1)

# rh(3,5)
# hr(5,1)







# hr(3,1)

# # empty 2 second
# rh(2,0)
# rh(2,5)
# hr(5,1)
# rh(2,1)


# rh(2,3)
# hr(7,2)

# rh(3,5)
# hr(5,1)

# hr(9,2)

# rh(3,9)

# rh(3,7)
# hr(7,2)
# rh(3,5)
# hr(5,1)

# hr(3,3)


# # empty A first
# rh(0,0)
# rh(0,10)
# rh(0,9)

# fork 2, c to 1
# rh(0,1)
# rh(2,5)
# hr(5,0)
# DEAD END

# fork 1, c to 7
# rh(0,7)
# hr(0,0)
# rh(2,5)
# hr(5,0)
# DEAD END























# rh(2,1) #
# hr(7,2)

# rh(1,)
# rh(1,5)
# hr(5,3)
# hr(1, 3)
# move(r,h,1,10)
# move(r,h,1,9)
# move(r,h,1,5)
# move(r,h,1,1)

# move(h,r,5,1)
# move(r,h,3,5)
# move(h,r,5,1)

# print("\n\n\nend, total cost:", total_cost)
# display_burrow(rooms, hall, 0)


























# # tyal 2 --> 55737
# move_room_to_hall(3, 1) #maybe b?
# move_room_to_hall(3, 2)
# move_room_to_hall(3, 11)
# move_room_to_hall(3, 10)
# move_room_to_hall(2, 8)
# move_room_to_room(2,3)
# move_room_to_hall(2,4)
# move_room_to_room(2,3)
# move_hall_to_room(4,2)
# move_hall_to_room(2,2)
# move_hall_to_hall(8,2)
# move_room_to_room(4,2)
# move_room_to_hall(4,4)
# move_room_to_room(4,3)
# move_room_to_room(4,2)
# move_hall_to_room(10,4)
# move_hall_to_hall(4,10)
# move_hall_to_room(2,4)
# move_room_to_hall(1,2)
# move_room_to_room(1,4)
# move_room_to_room(1,4)
# move_room_to_room(1,3)
# move_hall_to_room(2,1)
# move_hall_to_room(1,1)
# move_hall_to_room(10,1)
# move_hall_to_room(11,1)
# move_hall_to_room(1,1)
# move_hall_to_hall
# move_room_to_room



# old version no good --> 81977
# move_room_to_hall(1, 1)
# move_room_to_hall(1, 11)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 1, 10)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 3, 2)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 1, 8)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 2, 1)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 1, 1)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 3, 1) #2?
# rooms, hall, cost = move_room_to_room(rooms, 3, 1)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 3, 2)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 2, 4)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 8, 3)
# rooms, hall, cost = move_room_to_room(rooms, 2, 3)
# rooms, hall, cost = move_room_to_hall(rooms, hall, 2, 8)
# rooms, hall, cost = move_room_to_room(rooms, 2, 3)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 8, 2)
# rooms, hall, cost = move_room_to_room(rooms, 4, 2)
# rooms, hall, cost = move_hall_to_hall(hall, 4, 8)
# rooms, hall, cost = move_hall_to_hall(hall, 2, 6)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 1, 2)
# rooms, hall, cost = move_hall_to_hall(hall, 6, 1)
# rooms, hall, cost = move_hall_to_hall(hall, 8, 2)
# rooms, hall, cost = move_room_to_room(rooms, 4, 1)
# rooms, hall, cost = move_room_to_room(rooms, 4, 3)
# rooms, hall, cost = move_room_to_room(rooms, 4, 2)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 1, 4)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 2, 4)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 10, 4)
# rooms, hall, cost = move_hall_to_room(rooms, hall, 11, 4)


# Attempt 1
# rooms, hall, cost = move_room_to_hall(rooms, 1, hall, 1)
# rooms, hall, cost = move_room_to_hall(rooms, 3, hall, 2)
# rooms, hall, cost = move_room_to_hall(rooms, 4, hall, 11)
# rooms, hall, cost = move_room_to_hall(rooms, 3, hall, 10)

# as hall to hall

# move(r,h,4,1)
# move(r,h,4,11)
# move(r,h,4,10)
# move(r,h,4,2)
# move(r,r,2,4)

# move(r,h,2,8)
# move(r,h,2,4)
# move(r,h,2,6)

# move(h,r,4,2)
# move(h,r,2,2)
# move(h,r,1,2)

# move(h,h,6,1)
# move(r,h,3,2)
# move(r,r,3,2)

# move(r,h,3,4)
# move(h,h,8,6)
# move(r,r,3,4)

# move(h,r,6,3)
# move(h,r,10,3)

# move(h,h,4,10)
# move(h,h,2,8)

# move(h,r,1,3)

# move(r,h,1,1)
# move(h,h,8,2)
# move(r,r,1,4)
# move(r,r,1,4)
# move(r,r,1,3)

# move(h,r,2,1)
# move(h,r,1,1)
# move(h,r,10,1)
# move(h,r,11,1)



# def move_hall_to_hall(hall_index_1, hall_index_2):
#   global total_cost
#   hall_index_1 -= 1
#   hall_index_2 -= 1
#   shrimp = hall[hall_index_1]
#   hall[hall_index_1] = '..'
#   hall[hall_index_2] = shrimp

#   hall_cost = abs(hall_index_1-hall_index_2)
#   multiplier = energy_dict[shrimp[0]]
#   cost = multiplier*(hall_cost) 
#   total_cost += cost

#   output(cost)


# def move_room_to_room(room_index_1, room_index_2):
#   global total_cost
#   room_index_1 -= 1
#   room_index_2 -= 1
#   shrimp = rooms[room_index_1].pop(0)
#   rooms[room_index_2] = [shrimp] + rooms[room_index_2]

#   room_x_value_1 = 2 + (2*room_index_1)
#   room_x_value_2 = 2 + (2*room_index_2)
#   hall_cost = 2*abs(room_index_1-room_index_2)
#   room_cost_1 = 4 - len(rooms[room_index_1])
#   room_cost_2 = 5 - len(rooms[room_index_2])
#   multiplier = energy_dict[shrimp[0]]
#   cost = multiplier*(room_cost_1 + room_cost_2 + hall_cost)
#   total_cost += cost
#   output(cost)