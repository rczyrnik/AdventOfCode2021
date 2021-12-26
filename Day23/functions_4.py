# def read_data(file_name):
# 	file = open(file_name, 'r')
# 	raw_lines = file.readlines()
# 	file.close()
# 	return [line.strip() for line in raw_lines]

# 


def get_burrow(star):
  if star == 4:
    room2 = ['A', 'D', 'D', 'C']
    room4 = ['D', 'C', 'B', 'C']
    room6 = ['A', 'B', 'A', 'D']
    room8 = ['B', 'A', 'C', 'B']
  if star == 2:
    room2 = ['A', 'C']
    room4 = ['D', 'C']
    room6 = ['A', 'D']
    room8 = ['B', 'B']
  available_rooms = [2, 4, 6, 8]
  total_cost = [0]
  steps = []
  # return [['.'],['.'],room2,['.'],room4,['.'],room6,['.'],room8,['.'],['.'],available_rooms, total_cost]
  return [[],[],room2,[],room4,[],room6,[],room8,[],[],available_rooms, total_cost, steps]


def display_burrow(burrow, star):

  h0, h1, r2, h3, r4, h5, r6, h7, r8, h9, h10, _, _ = burrow.copy()

  #  pad to full length for display
  r2 = ['.'] * (star - len(r2)) + r2
  r4 = ['.'] * (star - len(r4)) + r4
  r6 = ['.'] * (star - len(r6)) + r6
  r8 = ['.'] * (star - len(r8)) + r8

  if len(h0) == 0: h0 = '.'
  else: h0 = h0[0]

  if len(h1) == 0: h1 = '.'
  else: h1 = h1[0]

  if len(h3) == 0: h3 = '.'
  else: h3 = h3[0]

  if len(h5) == 0: h5 = '.'
  else: h5 = h5[0]

  if len(h7) == 0: h7 = '.'
  else: h7 = h7[0]

  if len(h9) == 0: h9 = '.'
  else: h9 = h9[0]

  if len(h10) == 0: h10 = '.'
  else: h10 = h10[0]

  print('  0 1 2 3 4 5 6 7 8 9 10 ')
  print('#########################')

  # hall
  print("# {} {}   {}   {}   {}   {} {} #".format(h0, h1, h3, h5, h7, h9, h10))
  

  #rooms
  print('##### {} # {} # {} # {} #####'.format(r2[0], r4[0], r6[0], r8[0]))
  for i in range(1,star): print('    # {} # {} # {} # {} #  '.format(r2[i], r4[i], r6[i], r8[i]))
  print('    #################  ')
  print('      2   4   6   8    ')

  print()
  print()




def get_eligible_rooms(burrow, hall_index):
  available_rooms = burrow[11]
  eligible_rooms = []

  # go right
  index = hall_index
  while index < 9:
    if index%2 == 1 and burrow[index] == [] and index + 1 in available_rooms: eligible_rooms.append(index + 1)
    if index%2 == 1 and burrow[index] != []: index = 10
    index += 1

  # go left
  index = hall_index
  while index > 1:
    if index%2 == 1 and burrow[index] == [] and index - 1 in available_rooms: eligible_rooms.append(index - 1)
    if index%2 == 1 and burrow[index] != []: index = 0
    index -= 1
  
  return(eligible_rooms)