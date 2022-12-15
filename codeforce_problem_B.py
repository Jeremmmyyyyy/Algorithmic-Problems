import heapq
import math

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
        adjList[road[3] - 1].append((road[2], road[0]))
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
        if maxSnow < newElem[0] and findSet(connectedComp, start - 1) == findSet(connectedComp, end - 1):
            break
        maxSnow = newElem[0]
        union(connectedComp, newElem[2] - 1, newElem[3] - 1)
        #* pushes the roads that are valid in the heapq ordered by length.
        lengthList.append((newElem[1], newElem[0], newElem[2], newElem[3]))

    if findSet(connectedComp, start - 1) != findSet(connectedComp, end - 1):
        print("Impossible")
        exit()
        
    #* creates adjList to easier access to the neighbor vertex when uisng djikstra
    adjList = adjacencyList(intersections, lengthList)
    #* init the mist with max val
    Q = []
    #* init the source to 0
    for i in range(1, intersections + 1):
        if i == start:
            heapq.heappush(Q, (0, i))
        else:
            heapq.heappush(Q, (math.inf, i))

    distances = [math.inf for i in range(intersections)]
    distances[start-1] = 0

    while len(Q) != 0:
        u = heapq.heappop(Q)

        for dest in adjList[u[1] - 1]:
            if distances[dest[0] - 1] > distances[u[1] - 1] + dest[1]:
                distances[dest[0] - 1] = distances[u[1] - 1] + dest[1]
                heapq.heappush(Q, (distances[dest[0] - 1], dest[0]))
    
    return maxSnow, distances[end - 1]

if __name__ == '__main__':
    #* get the input from stdin
    intersections, n_roads, start, end, roads = getInput()

    # intersections = 4
    # n_roads = 4
    # start = 1
    # end = 4
    # roads=[(1, 3 , 100, 1),(1,2,2,1),(3,4,1,2),(2,3,2,2)]

    if start == end:
        print(0, 0)
        exit()
    if n_roads == 0:
        print("Impossible")
        exit()
    maxSnow, distance = optimized_path(intersections, n_roads, start, end, roads)    
    if distance == math.inf:
        print("Impossible")
    else:
        print(maxSnow, distance)
