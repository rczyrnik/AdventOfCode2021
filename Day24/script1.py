from functions import *


file_name = 'input1.txt'
data = read_data(file_name)

# model = [int(x) for x in list('13579246899999')]
# model = [5]
value_dict = {'w':0,'x':0,'y':0,'z':0}
for x in range(-30,30): value_dict[str(x)] = x

data_index = 1

# start set to 0
inputs = {(0,0,0,0): 0}


def one_cycle(inputs, data_index, value_dict):
    outputs = {}
    # cycle through the prevous step's outputs (now this step's inputs)
    for variables, number in inputs.items():

        # cycle through all the digits
        for current_value in range(10):
            # assign the values of this version (one of the outpus from the previous row)
            i = data_index
            value_dict['w'], value_dict['x'], value_dict['y'], value_dict['z'] = variables[0], variables[1], variables[2], variables[3]
            
            # by construction, first line always 'inp w'
            value_dict['w'] = current_value
            line = data[i]
            while line[:3] != 'inp':
                line = data[i]
                value_dict = process_line(line, value_dict, current_value)
                i += 1
            i += 1
            output = (value_dict['w'], value_dict['x'], value_dict['y'], value_dict['z'])

            # add to dictionary
            outputs[output] = number*10 + current_value
    return(outputs, i)

for x in range(10):
    inputs, data_index = one_cycle(inputs, data_index, value_dict)
    print(len(inputs))
# print(inputs)
print(len(inputs))