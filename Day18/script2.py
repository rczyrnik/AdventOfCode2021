n = [[[[[9,8],1],2],3],4] #/--> [[[[0,9],2],3],4]

# for a in range(len(n)):
#     print(n[a])


# print(n[0][0][0][0][0])  # 9
# print(n[0][0][0][0][1])  # 9
# print(n[0][0][0][1]) #1
# print(n[0][0][1]) #2
# print(n[0][1]) #3
# print(n[1])

def replace_in_w_list(n):
    for a in range(len(n)):
        if isinstance(n[a], int): n[a] = [n[a]]
        elif isinstance(n[a], list): replace_in_w_list(n[a])
    return(n)

n = replace_in_w_list(n)
print(n)
