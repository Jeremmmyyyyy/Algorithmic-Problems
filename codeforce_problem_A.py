import sys

#* Input management
def getInput():
    n_posts, n_hitch, gas = map(int, input().split())
    if n_posts < 2 or n_posts > 2000 or n_hitch < 0 or n_hitch > 2000 or gas < 0 or gas > 10**9:
        return - 1
    hitchhickers = []
    for i in range(0, n_hitch):
        start, end, food, gasol = map(int, input().split())
        if start < 1 or start > (n_posts - 1) or end < 2 or end > n_posts or food < 0 or food > 10**9 or gas < 0 or gas > 10**9:
            return - 1
        hitchhickers.append((start, end, food, gasol))
    
    return n_posts, n_hitch, gas, hitchhickers

#? Recursive function doing all the computations 
def memorized_mad_max_aux(posts, gasAvailable, M, T, maxVal):
    #* input starts with 1 so we shift by -1 so that we get a correct indice for indexing in the tables
    index = posts - 1
    #* if the number of posts we have to compute is reached we have to stop the recursion
    if posts >= maxVal:
        result = 0
    else:
        result = -1
        result1 = -1
        result2 = -1
        #* if there are hitchhickers on post index
        if len(T[index]) > 0:
            #* Iterate over the number of hitchhickers
            for i in range(len(T[index])):
                #* compute the gas at position index + the gas given by the hitchhicker
                currentGasPlusHhGas = gasAvailable + T[index][i][3]
                #* if the gas is greater than the amount of gas needed to do the jump :
                if currentGasPlusHhGas >= T[index][i][1] - T[index][i][0]:
                    #! OPTIMIZATION : if the gas is greater than the number of posts we know that we can reach the end so we have to resize the gas to avoid useless computations
                    if currentGasPlusHhGas >= maxVal - index:
                        currentGasPlusHhGas = maxVal - index
                    #! OPTIMIZATION : check in the table before making the recursive call avoid unnecessary call
                    alreadyComp = [(gas,food) for gas, food in M[T[index][i][1] - 1] if gas  == currentGasPlusHhGas - (T[index][i][1] - T[index][i][0])]
                    if len(alreadyComp) == 1:
                        result2 = alreadyComp[0][1]
                    else:
                        #* Compute the result of the jump with hitchhicker i
                        result2 = memorized_mad_max_aux(T[index][i][1], currentGasPlusHhGas - (T[index][i][1] - T[index][i][0]), M, T, maxVal)
                    foodBonus = T[index][i][2]
                    #* if the result is -1 we can't reach the end so we have to retrun -1
                    if result2 + foodBonus < foodBonus:
                        result = -1
                    #* else return the max
                    else:                
                        result = max(result, result1, result2 + foodBonus)
            #* if there is no hitchhicker but gas is greater than 0 we can move forward 
            if gasAvailable > 0:
                #! OPTIMIZATION if there are no hitchhickers for a long period of posts we can do a bigger jump and avoid computations
                #* Compute the biggest possible jump
                nextHh = index + 1
                while len(T[nextHh]) == 0 and nextHh < gasAvailable and nextHh < len(T) - 1:
                    nextHh += 1
                jump = nextHh - index
                #* compute the recursion with the jump directly
                alreadyComp = [(gas,food) for gas, food in M[index + jump] if gas  == gasAvailable - jump]
                if len(alreadyComp) == 1:
                    result1 = alreadyComp[0][1]
                else:
                    result1 = memorized_mad_max_aux(posts + jump, gasAvailable - jump, M, T, maxVal)
                result = max(result, result1)
        #* if there is no hitchhicker but gas is greater than 0 we can move forward same as before
        elif gasAvailable > 0:

            nextHh = index + 1
            while len(T[nextHh]) == 0 and nextHh < gasAvailable and nextHh < len(T) - 1:
                nextHh += 1
            jump = nextHh - index

            alreadyComp = [(gas,food) for gas, food in M[index + jump] if gas  == gasAvailable - jump]
            if len(alreadyComp) == 1:
                result = alreadyComp[0][1]
            else:
                result = memorized_mad_max_aux(posts + jump, gasAvailable - jump, M, T, maxVal)
        #* if there is no hitchhicker and no more gas we can't reach the end so output impossible
        else:
            result = -1
    #* stores the result at right position and return
    M[index].append((gasAvailable, result))
    return result

#? main recursion for the problem
def memorized_mad_max(n_posts, gas, hitchhickers):
    sys.setrecursionlimit(5000)
    if n_posts == 0:
        return 0
    else:
        #* newTable contains the at index i the list of hitchhickers waiting at position i
        newTable = []
        #* m is an empty array of size n_posts * n_posts used to store our computations
        m = []
        for i in range(n_posts):
            newTable.append([])
            m.append([])
        maxFood = 0
        maxFuel = gas
        for index, value in enumerate(hitchhickers):
            maxFood += value[2]
            maxFuel += value[3]
            newTable[value[0] - 1].append(value)
            if value[0] == value [1]:
                return - 1
        #! OPTIMIZATION : if certain conditions arrise we can directly output the result
        if gas >= n_posts:
            gas = n_posts
        if maxFuel < n_posts - 1:
            return -1
        elif maxFood == 0 and maxFuel >= n_posts:
            return 0
        else:
            #* else call the recursive function to solve the problem
            return memorized_mad_max_aux(1, gas, m, newTable, n_posts)


if __name__ == '__main__':
    #! OPTIMIZATION : python allows a max of 1000 recursions the biggest valid input can lead to up to 2000 recursions so we need to change the bound
    sys.setrecursionlimit(5000)
    try:
        #* get the input from stdin
        n_posts, n_hitch, gas, hitchhickers = getInput()
    except:
        print("Impossible")
    else:
        #* call the recursion
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        #* if the result is less than 0 (-1) output Impossible
        if res < 0:
            print("Impossible")
        #* else print the result
        else:
            print(res)