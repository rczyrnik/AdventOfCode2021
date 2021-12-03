file = open('data2.csv', 'r')
lines = file.readlines()
file.close()

previous = 0
current = 0
count = -1

for line in lines: 
	current = int(line.strip())
	if current > previous:
		count += 1
	previous = current

print(count):