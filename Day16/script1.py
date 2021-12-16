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

def type_4(byte_list):
    binary_list = []
    start = 6
    leading_digit = '1'
    while leading_digit == '1':
        five_digits = byte_list[start:start+5]
        leading_digit = five_digits[0]
        binary_list += five_digits[1:]
        start += 5
    final_number = bin_to_dec(binary_list)
    return (final_number, byte_list[start:])


# --~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~
number_to_binary = get_number_to_binary()
binary_to_number = get_binary_to_number(number_to_binary)
binary_dict_3  = get_binary_dict_3()
# READ FILE
file_name = "operator_packet.txt"
# file_name = "example1.txt"     # D2FE28
# file_name = "example2.txt"   # 38006F45291200
# file_name = "example3.txt"   # EE00D40C823060
file_name = "example4.txt"   # 8A004A801A8002F478
# file_name = "example5.txt"   # 620080001611562C8802118E34
# file_name = "example6.txt"   # C0015000016115A2E0802F182340
# file_name = "example7.txt"   # A0016C880162017C3686B18A3D4780

# print(file_name)
packet = read_data(file_name)[0]
byte_list = packet_to_bytes(packet)
print(''.join(byte_list))
def process_byte_list(byte_list):
    version = binary_dict_3[tuple(byte_list[0:3])]
    type_id = binary_dict_3[tuple(byte_list[3:6])] 

    if type_id == 4:
        print("\nTYPE 4 LITERAL")  
        number, byte_list = type_4(byte_list)
        print(number, byte_list, end = "\n")
        return(number, byte_list)
    else:
        length_type_id = byte_list[6]
        if length_type_id == '0': 
            print("\nTYPE X OPERATOR, LENGTH")  
            byte_length = 15
            length_of_subpackets = bin_to_dec(byte_list[7:7+byte_length])
            packet = byte_list[7+byte_length: 7+byte_length+length_of_subpackets]
            while len(packet) > 0:
                number, packet = type_4(packet)
                print(number)
        elif length_type_id == '1': 
            print("\nTYPE X OPERATOR, COUNT")  
            byte_length = 11
            num_of_subpackets = bin_to_dec(byte_list[7:7+byte_length])
            print("num of sub packets: ", num_of_subpackets)

            new_packet = byte_list[7+byte_length:]
            
            print("new_packet: ", ''.join(new_packet))
            for x in range(num_of_subpackets):
                number, new_packet = type_4(new_packet)
                print(number)
        # print(length_type_id, byte_length, length_of_subpackets)
        # print(''.join(subpacket))
        # return(packet)


process_byte_list(byte_list)
# # print("new_byte_list: ", new_byte_list)
# # process_byte_list(new_byte_list)