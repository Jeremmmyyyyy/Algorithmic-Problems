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

def findSet(set):
    if set != set[1]:
        set[1] = findSet(set[1])
    return set[1]

def link(set1, set2):
    if set1[2] > set2[2]:
        set2[1] = set1[0]
    else:
        set1[1] = set2[0]
        if set1[2] == set2[2]:
            set2[2] = set2[2] + 1

def union(set1, set2):
    link(findSet(set1), findSet(set2))

def adjacencyList(n_intersections, roads):
    adjList = [[] for i in range(n_intersections)]
    for road in roads:
        adjList[road[2]].append((road[3], road[0]))
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
    for i in range(n_roads):
        newElem = heapq.heappop(heapqSnow)
        union(connectedComp[newElem[2]], connectedComp[newElem[3]])
        #* pushes the roads that are valid in the heapq ordered by length.
        lengthList.append((newElem[1], newElem[0], newElem[2], newElem[3]))
        if findSet(connectedComp[start]) == findSet(connectedComp[end]):
            break
        
    #* creates adjList to easier access to the neighbor vertex when uisng djikstra
    adjList = adjacencyList(intersections, lengthList)
    #* init the mist with max val
    Q = [[(10**10, i)] for i in range(intersections)]
    #* init the source to 0
    Q[start][0] = 0
    S = []
    while len(Q) != 0:
        u = heapq.heappop(Q)
        S.append(u)
        for dest in adjList[u[1]]:
            if Q[dest[0]] > u[0] + dest[1]:
                Q[dest[0]][0] = u[0] + dest[1]
                heapq.heapify(Q)
    
    length = [length for (length, id) in Q if id == end]
    return end

if __name__ == '__main__':
    #* get the input from stdin
    intersections, n_roads, start, end, roads = getInput()
    optimized_path(intersections, n_roads, start, end, roads)
    
        
