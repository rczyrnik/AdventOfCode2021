from functions import *

file_name = 'input4.txt'
data = read_data(file_name)


grid = make_grid()

# line = 'on x=10..12,y=10..12,z=10..12'

# data = ['on x=967..23432,y=45373..81175,z=27513..53682']
for line in data:
    on_off,x1,x2,y1,y2,z1,z2 = decode_line(line)
    # print(on_off,x1,x2,y1,y2,z1,z2 )
    grid = update_grid(grid,on_off,x1,x2,y1,y2,z1,z2)
print(count_on(grid))


