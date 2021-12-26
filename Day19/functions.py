
def sort_beacons(beacons):
    continue_ = True
    while continue_:
        for i in range(len(beacons)-1):
            print(i, beacons[i])
            current_beacon = beacons[i]
            if current_beacon > beacons[i+1]:
                continue_ = True
                beacons[i] = beacons[i+1]
                beacons[i+1] = current_beacon
            elif current_beacon == beacons[i+1]:
                print('time to cross the bridge')
            else:
                continue_ = False
        return(beacons)

def distance(beacon1, beacon2):
    x = beacon2[0] - beacon1[0]
    y = beacon2[1] - beacon1[1]
    return( round((x**2 + y**2)**(1/2), 6))

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]


def get_scanner_list(file_name):
    raw_data = read_data(file_name)
    scanner_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    scanner_no = -1
    for line in raw_data:
        if len(line) > 16:
            scanner_no += 1
        elif len(line) > 1:
            scanner_list[scanner_no].append(tuple([int(x) for x in line.split(',')]))
    return([x for x in scanner_list if x != []])



# --- scanner 0 ---
# 0,2
# 4,1
# 3,3
# -6,-9

# --- scanner 1 ---
# -1,-1
# -5,0
# -2,1
# 3,5