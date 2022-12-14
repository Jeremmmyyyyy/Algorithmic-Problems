import heapq

#* Input management
def getInput():
    intersections, n_roads, start, end = map(int, input().split())
    roads = []
    for i in range(0, n_roads):
        r_start, r_end, length, snow = map(int, input().split())
        roads.append((r_start, r_end, length, snow))
    return intersections, n_roads, start, end, roads

def makeSet(number):
    #* set, parent, rank
    return [[i , i, 0] for i in range(number)]

def findSet(l, x):
    if l[x][0] != l[x][1]:
        l[x][1] = findSet(l, l[x][1])
    return l[x][1]

def link(l, x, y):
    if l[x][2] > l[y][2]:
        l[y][1] = x
    else:
        l[x][1] = y
        if l[x][2] == l[y][2]:
            l[y][2] = l[y][2] + 1

def union(l, x, y):
    link(l, findSet(l, x), findSet(l, y))

def adjacencyList(n_intersections, roads):
    adjList = [[] for i in range(n_intersections)]
    for road in roads:
        adjList[road[2] - 1].append((road[3], road[0]))
    return adjList

def optimized_path(intersections, n_roads, start, end, roads):
    
    #* creates heap containing the elements stored by increasing snow amount
    heapqSnow = []
    for (r_start, r_end, length, snow) in roads:
        heapq.heappush(heapqSnow, (snow, length, r_start, r_end))

    #* create heapq for the length of the chosen roads
    lengthList = []
    #* create a set for each intersection
    connectedComp = makeSet(intersections)
    #* Iterate over all the roads. And connect the sets that are connected by the roads
    #* this connection process takes all the smallest roads and stops when the start point and end point are connected
    #* result in a list of roads with minimum maximum amount of snow that connects end point s and t
    maxSnow = -1
    for i in range(n_roads):
        newElem = heapq.heappop(heapqSnow)
        union(connectedComp, newElem[2] - 1, newElem[3] - 1)
        #* pushes the roads that are valid in the heapq ordered by length.
        lengthList.append((newElem[1], newElem[0], newElem[2], newElem[3]))
        if findSet(connectedComp, start - 1) == findSet(connectedComp, end - 1):
            maxSnow = newElem[0]
            break
        
    #* creates adjList to easier access to the neighbor vertex when uisng djikstra
    adjList = adjacencyList(intersections, lengthList)
    #* init the mist with max val
    Q = []
    #* init the source to 0
    heapq.heappush(Q, (0, start - 1))
    for i in range(1, intersections):
        heapq.heappush(Q, (10**10, i))
    S = []
    while len(Q) != 0:
        u = heapq.heappop(Q)
        S.append(u)
        for dest in adjList[u[1]]:
            # tup = [end for i in Q if i[1] == dest[0] - 1]
            if Q[dest[0] - 1][0] > u[0] + dest[1]:
                Q[dest[0] - 1] = (u[0] + dest[1], Q[dest[0] - 1][1])
    
    length = [length for (length, id) in Q if id == end]
    return maxSnow, end

if __name__ == '__main__':
    #* get the input from stdin
    # intersections, n_roads, start, end, roads = getInput()
    intersections = 3
    n_roads = 3
    start = 1 
    end = 3
    roads = [(1, 3, 1, 3), (1, 2, 10, 1), (2, 3, 10, 2)]
    optimized_path(intersections, n_roads, start, end, roads)
    
        
