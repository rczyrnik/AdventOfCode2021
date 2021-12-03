file = open('data2.csv', 'r')
lines = file.readlines()
file.close()

horizontal = 0
depth = 0
aim = 0

direction = ''
amount = 0

for line in lines:
	[direction, amount] = line.split()
	if direction == "forward":
		horizontal += int(amount)
		depth += aim * int(amount)
	elif direction == "up":
		aim -= int(amount)
	elif direction == "down":
		aim += int(amount)
	else:
		print("ERROR, unknown direction")

print(horizontal*depth)
