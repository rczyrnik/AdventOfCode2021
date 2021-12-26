def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]
def calculate(fn, a, b):
    if fn == 'inp': return(a)
    elif fn == 'add':  return(a+b)
    elif fn == 'mul':  return(a*b)
    elif fn == 'div': return(a//b)
    elif fn == 'mod': return(a%b)
    elif fn == 'eql':
        if a==b:  return(1)
        else:  return(0)


def process_line(line, value_dict, current_value):
    split = line.split(' ')
    # print(split, end = ' --> ')
    if len(split) == 2:
        value_dict[split[1]] = current_value
    else:
        fn = split[0]
        a = value_dict[split[1]]
        b = value_dict[split[2]]
        value_dict[split[1]] = calculate(fn, a, b)
    # print(split[1], "=", values[split[1]])
    return(value_dict)

