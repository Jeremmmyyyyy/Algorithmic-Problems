import sys

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


def memorized_mad_max_aux(posts, gasAvailable, M, T, maxVal):
    index = posts - 1

    # alreadyComp = [(gas,food) for gas, food in M[index] if gas  == gasAvailable]
    # if len(alreadyComp) == 1:
    #     return alreadyComp[0][1]
    
    if posts >= maxVal:
        result = 0
    else:
        result = -1
        result1 = -1
        result2 = -1
        
        if len(T[index]) > 0:

            for i in range(len(T[index])):

                currentGasPlusHhGas = gasAvailable + T[index][i][3]
                if currentGasPlusHhGas >= T[index][i][1] - T[index][i][0]:

                    if currentGasPlusHhGas >= maxVal - index:
                        currentGasPlusHhGas = maxVal - index
                    
                    alreadyComp = [(gas,food) for gas, food in M[T[index][i][1] - 1] if gas  == currentGasPlusHhGas - (T[index][i][1] - T[index][i][0])]
                    if len(alreadyComp) == 1:
                        result2 = alreadyComp[0][1]
                    else:
                        result2 = memorized_mad_max_aux(T[index][i][1], currentGasPlusHhGas - (T[index][i][1] - T[index][i][0]), M, T, maxVal)
                
                    foodBonus = T[index][i][2]
                    if result2 + foodBonus < foodBonus:
                        result = -1
                    else:                
                        result = max(result, result1, result2 + foodBonus)

            if gasAvailable > 0:

                nextHh = index + 1
                while len(T[nextHh]) == 0 and nextHh < gasAvailable and nextHh < len(T) - 1:
                    nextHh += 1
                jump = nextHh - index

                alreadyComp = [(gas,food) for gas, food in M[index + jump] if gas  == gasAvailable - jump]
                if len(alreadyComp) == 1:
                    result1 = alreadyComp[0][1]
                else:
                    result1 = memorized_mad_max_aux(posts + jump, gasAvailable - jump, M, T, maxVal)
                result = max(result, result1)

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

        else:
            result = -1

    M[index].append((gasAvailable, result))
    return result


def memorized_mad_max(n_posts, gas, hitchhickers):
    if n_posts == 0:
        return 0
    else:
        newTable = []
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
        if gas >= n_posts:
            gas = n_posts

        if maxFuel < n_posts - 1:
            return -1
        elif maxFood == 0 and maxFuel >= n_posts:
            return 0
        else:
            return memorized_mad_max_aux(1, gas, m, newTable, n_posts)


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    try:
        n_posts, n_hitch, gas, hitchhickers = getInput()
    except:
        print("Impossible")
    else:

        res = memorized_mad_max(n_posts, gas, hitchhickers)
        if res < 0:
            print("Impossible")
        else:
            print(res)