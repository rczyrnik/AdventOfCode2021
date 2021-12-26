from functions import *

# --- scanner 0 ---
# 0,2 A
# 4,1 C
# 3,3 B

# --- scanner 1 ---
# -1,-1 C
# -5,0 A
# -2,1 B


file_name = 'input2.txt'
scanner_list = get_scanner_list(file_name)

def get_distance_dict(beacons):
    dist_dict = {}
    for beacon1 in beacons:
        dist_dict[tuple(beacon1)] = []
        for beacon2 in beacons:
            dist_dict[tuple(beacon1)].append(distance(beacon1, beacon2))
    return(dist_dict)

scanner_dist_list = []
for scanner in scanner_list:
    scanner_dist_list.append(get_distance_dict(scanner))
print(scanner_dist_list)

# the thinking is, the distance has to match with another for at least 12 (/3) to be included
scanner_magoo = scanner_list[0]
scanner_todo = scanner_list[1]
scanner_todo_dist_list = scanner_dist_list[1]
# print(scanner_magoo)

for beacon in scanner_magoo:
    print(scanner_todo_dist_list)
