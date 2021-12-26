import heapq
from copy import deepcopy
depth=4#depth=2 for Part 1, 4 for Part 2
#Part 1:
#stateandval=(0,(4,-2),(8,-2),(2,-2),(6,-2),(6,-1),(8,-1),(2,-1),(4,-1))
#Part 2
stateandval=(0,(4,-4),(6,-3),(8,-2),(8,-4),(2,-4),(4,-3),(6,-2),(6,-4),(4,-2),(6,-1),(8,-1),(8,-3),(2,-1),(2,-2),(2,-3),(4,-1))#0th element is energy so far stateandval[1:] are coordinates of all As then all Bs then all Cs then all Ds
dests=[x for x in [(x,0) for x in range(11)]+[(a,b) for a in range(2,9,2) for b in range(-depth,0)] if not((x[0] in [2,4,6,8]) and x[1]==0)]
dist={(x,y):int(int(abs(x[0]-y[0])+abs(x[1]-y[1]))) for x in dests for y in dests  if not((x[1]<0 and y[1]<0)) and not (x[1]==0 and y[1]==0)}
blocks={w:[z for z in dests if z[0] in range(min(w[0][0],w[1][0])+1,max(w[0][0],w[1][0])) and z[1]==0]+list(set([w[1]]+[(z[0],z[1]+j) for j in range(1,depth) for z in w if z[1]+j<0  ])) for w in dist}
hall=[x for x in dests if x[1]==0]
rooms=[x for x in dests if x[1]<0]
goals={k:sorted([(2*(k+1),-j) for j in range(1,depth+1)]) for k in range(4)}

goal=[set(goals[k]) for k in range(4)]
def flatten(state):
    state=[sorted(y) for y in state]
    return(tuple([x for y in state for x in y])) 

def expand(state):
    size=len(state)//4
    return([list(state[i*size:(i+1)*size]) for i in range(4)])

def heuristic(exp):
    return(sum([abs(z[0]-2*(i+1)) for i in range(4) for z in exp[i] ]))

def neighbors(cur):
    occupied=[x for y in cur for x in y]
    newstates=[]
    plusen=[]
    
    ready=[len([ y for j in range(4) for y in cur[j] if j!=k and y in goals[k]])==0 for k in range(4)]#check if we can start going back into this room now
    for k,let in enumerate(cur):
        if not len([x for x in let if x in goals[k]])==depth:#haven't filled this room yet
            for j,l in enumerate(let):              
                    if l in rooms and (j!=k or (j==k and not(ready[k]))):#try moving to the hall if appropriate
                        for h in hall:
                            if len([x for x in occupied if x in blocks[(l,h)]])==0:#make sure the path is clear
                                tmp=deepcopy(cur)
                                tmp[k][j]=h
                                newstates.append(deepcopy(tmp))
                                plusen.append(dist[(l,h)]*(10**k))            
                    elif l in hall:#l is in the hall
                        if len([ y for x in range(4) for y in cur[x] if x!=k and y in goals[k] ])==0:#no other letters are in our room
                            gs=[x for x in goals[k] if x not in cur[k]]
                            if len(gs)>0 and len([x for x in occupied if x in blocks[(l,gs[0])]])==0:#is there an open spot in our room and if so, is the path clear?
                                tmp=deepcopy(cur)
                                tmp[k][j]=gs[0]
                                newstates.append(deepcopy(tmp))
                                plusen.append(dist[(l,gs[0])]*(10**k))
    return(newstates,plusen)

frontier=[]
heapq.heappush(frontier,stateandval)
seen={stateandval[1:]:stateandval[0]}
###Run A*###
while True:
    stuff=heapq.heappop(frontier)
    state=stuff[1:]
    exp=expand(state)
    if len([j for j in range(4) if set(exp[j])==goal[j]])==4:
        print(seen[state])
        break
    e=seen[state]
    neighs,energies=neighbors(exp)
    for i in range(len(neighs)):
        etot=e+energies[i]
        new=flatten(neighs[i])
        if new not in seen or seen[new]>etot:
            seen[new]=etot
            priority=etot+heuristic(neighs[i])
            heapq.heappush(frontier,tuple([priority]+[x for x in new]))
