file = open('data2.csv', 'r')
lines = file.readlines()
file.close()

list = [int(line.strip()) for line in lines]

previous = 0
current = 0
count = -1

for i in range(len(list)-2):
	current = list[i]+list[i+1]+list[i+2]
	if current > previous:
		count += 1
	previous = current

print(count)
