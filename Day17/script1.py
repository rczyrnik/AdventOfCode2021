v = [6,9] #no?
v = [7,2]
v = [6,3]
v = [9,0]
v = [6, 9]
p = [0,0]
# T = [20,30,-10,-5]
T = [185,221,-122,-74]
def step(p, v):
    p[0] += v[0]
    p[1] += v[1]
    if v[0] > 0:
        v[0] -= 1
    elif v[0] < 0:
        v[0] += 1
    v[1] -= 1
    return(p,v)

def within_target(p,T):
    if p[0] >= T[0] and p[0] <= T[1] and p[1] >= T[2] and p[1]<=T[3]:
        return True
    else:
        return False

# print(T)
# for _ in range(22):
#     p,v = step(p,v)
#     print(p, end = "")
#     print(within_target(p,T))


y_max_list = []
y_max = 0
count = 0
final_set = set()
for x in range(1,222):
    for y in range(-123,2000):
        v0 = [x,y]
        v = [x,y]
        p = [0,0]
        flag = False
        arc_max = 0
        while p[0]<T[1] and p[1] > T[2]:
        # for x in range(10):    
            p,v = step(p,v)
            # y = p[1]
            if p[1] > arc_max:
                arc_max = p[1]
            if within_target(p,T):
                flag = True
                # print("{},{}".format(v0[0], v0[1]))
                count += 1
                final_set.add(tuple(v0))
                if arc_max > y_max:
                    y_max = arc_max
print(v0, flag, arc_max, y_max, count)
print(final_set)
print(len(final_set))
        # y_max_list.append([x, y, y_max])
# print(y_max_list)
# print()