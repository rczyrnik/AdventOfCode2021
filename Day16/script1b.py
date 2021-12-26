def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

def get_number_to_binary():
    binary = read_data("binary.txt")
    number_to_binary = {}
    for line in binary:
        (num, dig) = line.split(" = ")
        number_to_binary[num] =  dig
    return (number_to_binary)

def get_binary_to_number(number_to_binary):
    binary_to_number = {}
    for key, value in number_to_binary.items():
        binary_to_number[tuple(value)] = key
    return (binary_to_number)

def get_binary_dict_3():
    return {('0','0','0'): 0,('0','0','1'): 1,('0','1','0'): 2,('0','1','1'): 3,
                 ('1','0','0'): 4,('1','0','1'): 5,('1','1','0'): 6,('1','1','1'): 7}

def bin_to_dec(binary_list):
    output = 0
    for i, digit in enumerate(binary_list[::-1]):
        output += int(digit) * (2**i)
    return(output)

def packet_to_bytes(packet):
    byte_list = []
    for letter in packet:
        # print(binary_dict[letter])
        byte_list += list(number_to_binary[letter])
    return byte_list

def type_4(packet):
    version = get_version(packet, position)
    binary_list = []
    start = position+6
    leading_digit = '1'
    while leading_digit == '1':
        five_digits = packet[start:start+5]
        leading_digit = five_digits[0]
        binary_list += five_digits[1:]
        start += 5
    final_number = bin_to_dec(binary_list)
    return (version, final_number, packet[start:])

def get_version(packet, position):
    version = binary_dict_3[tuple(packet[position+0:position+3])]
    print(version)
    return(version)
# --~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~
number_to_binary = get_number_to_binary()
binary_to_number = get_binary_to_number(number_to_binary)
binary_dict_3  = get_binary_dict_3()
# READ FILE
# file_name = "operator_packet.txt"
# file_name = "example1.txt"     # D2FE28 --> 6
# file_name = "example2.txt"   # 38006F45291200 --> 9(?)
# file_name = "example3.txt"   # EE00D40C823060 --> 14(?)
# file_name = "example4.txt"   # 8A004A801A8002F478 --> 16
# file_name = "example5.txt"   # 620080001611562C8802118E34 --> 12
# file_name = "example6.txt"   # C0015000016115A2E0802F182340 --> 23
# file_name = "example7.txt"   # A0016C880162017C3686B18A3D4780 --> 31
# file_name = "input1.txt"
raw_packet = read_data(file_name)[0]

# raw_packet = "C200B40A82" # finds the sum of 1 and 2, resulting in the value 3.
# raw_packet = "04005AC33890" # finds the product of 6 and 9, resulting in the value 54.
# raw_packet = "880086C3E88112" # finds the minimum of 7, 8, and 9, resulting in the value 7.
# raw_packet = "CE00C43D881120" # finds the maximum of 7, 8, and 9, resulting in the value 9.
# raw_packet = "D8005AC2A8F0" # produces 1, because 5 is less than 15.
# raw_packet = "F600BC2D8F" # produces 0, because 5 is not greater than 15.
# raw_packet = "9C005AC2F8F0" # produces 0, because 5 is not equal to 15.
# raw_packet = "9C0141080250320F1802104A08" # produces 1, because 1 + 3 = 2 * 2.

packet = packet_to_bytes(raw_packet)


def loop(packet, position):
    # print(position)
    type_id = type_id = binary_dict_3[tuple(packet[position+3:position+6])] 

    if type_id == 4:
        # print("TYPE 4, position = ", position)
        version = get_version(packet, position)
        position += 6
        leading_digit = packet[position]
        while leading_digit == '1': 
            position += 5
            leading_digit = packet[position]
        position += 5
        return(position)

    else:
        length_type_id = packet[position+6]

        if length_type_id == '0': 
            # print("TYPE LENGTH, position = {}".format(position))

            version = get_version(packet, position)
            length = bin_to_dec(packet[position+7:position + (7+15)])
            # print(length)
            position += (7+15)
            final_position = position + length
            while final_position-position > 0:
                position = loop(packet, position)

        elif length_type_id == '1':
            count = bin_to_dec(packet[position+7:position+7+11])
            # print("TYPE COUNT, position = {}, count = {}".format(position, count))
            version = get_version(packet, position)
            position += (7+11)
            for _ in range(count):
                # print("loop: ", _)
                position = loop(packet, position)

    return(position)

position = 0
loop(packet, position)