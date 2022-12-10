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
    if M[index][gasAvailable] != -1:
        return M[index][gasAvailable] 
    # if len(alreadyComp) == 1:
    #     return alreadyComp[0][1]
    # elif len(alreadyComp) > 1:
    #     maxFood = -1
    #     for elem in alreadyComp:
    #         if elem[1] >= maxFood:
    #             maxFood = elem[1]
    #     return maxFood
    
    if posts >= maxVal:
        result = 0
    else:
        result = -1
        result1 = -1
        result2 = -1
        
        if len(T[index]) > 0:
            if gasAvailable > 0:
                result1 = memorized_mad_max_aux(posts + 1, gasAvailable - 1, M, T, maxVal)
            for i in range(len(T[index])):
                currentGasPlusHhGas = gasAvailable + T[index][i][3]
                if currentGasPlusHhGas >= T[index][i][1] - T[index][i][0]:
                    if currentGasPlusHhGas >= maxVal - index:
                        currentGasPlusHhGas = maxVal - index
                    result2 = memorized_mad_max_aux(T[index][i][1], currentGasPlusHhGas - (T[index][i][1] - T[index][i][0]), M, T, maxVal)
                    foodBonus = T[index][i][2]
                    if result2 + foodBonus < foodBonus:
                        result = -1
                    else:                
                        result = max(result, result1, result2 + foodBonus)
        elif gasAvailable > 0:
            result = memorized_mad_max_aux(posts + 1, gasAvailable - 1, M, T, maxVal)
        else:
            result = -1

    if M[index][gasAvailable] < result:
        M[index][gasAvailable] = result
    return result


def memorized_mad_max(n_posts, gas, hitchhickers):
    if n_posts == 0:
        return 0
    else:
        newTable = []
        m = [[-1 for x in range(n_posts)] for y in range(n_posts)] 
        for i in range(n_posts):
            newTable.append([])
        maxFood = 0
        maxFuel = gas
        for index, value in enumerate(hitchhickers):
            maxFood += value[2]
            maxFuel += value[3]
            newTable[value[0] - 1].append(value)
            if value[0] == value [1]:
                return - 1
        if gas >= n_posts - 1:
            gas = n_posts - 1

        if maxFuel < n_posts - 1:
            return -1
        elif maxFood == 0 and maxFuel >= n_posts:
            return 0
        else:
            return memorized_mad_max_aux(1, gas, m, newTable, n_posts)

def tests(bool = False):
    if bool:
        n_posts = 3
        gas = 1
        hitchhickers = [(1, 3, 3, 2), (2, 3, 4, 1)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 4

        n_posts = 3
        gas = 0
        hitchhickers = [(1, 2, 3, 0), (2, 3, 4, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 3
        gas = 1
        hitchhickers = [(2, 3, 5, 0), (2, 3, 6, 0), (1, 3, 67, 5)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 67

        n_posts = 1
        gas = 0
        hitchhickers = [(0, 0, 5, 0), (0, 0, 6, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 1
        gas = 0
        hitchhickers = [(1, 1, 5, 0), (1, 1, 6, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 3
        gas = 1
        hitchhickers = [(3, 3, 5, 5)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 4
        gas = 1
        hitchhickers = [(1, 2, 10, 1), (3, 4, 1, 1), (1, 4, 100, 1)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 11

        n_posts = 10
        gas = 6
        hitchhickers = [(5, 6, 4, 2), (2, 8, 0, 4), (6, 8, 8, 9),
                        (1, 3, 0, 2), (3, 9, 6, 8), (6, 7,4, 9),
                        (8, 10, 6, 4), (8, 9, 2, 3), (2, 10, 0, 1),
                        (8, 10, 0, 1)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 18

        n_posts = 10
        gas = 6
        hitchhickers = [(5, 6, 4, 2), (6, 8, 8, 9),(8, 10, 6, 4)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 18

        n_posts = 10
        gas = 3
        hitchhickers = [(1, 6, 10, 8), (3, 7, 9, 9), (1, 5, 9, 10),
                        (1, 4, 0, 6), (4, 6, 10, 8), (3, 5, 0, 6),
                        (9, 10, 10, 8), (1, 7, 4, 0), (6, 10, 3, 1),
                        (1, 8, 5, 1)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 20

        n_posts = 10
        gas = 1
        hitchhickers = [(5, 7, 7, 6), (4, 5, 10, 0), (3, 10, 7, 8),
                        (8, 10, 0, 3), (4, 8, 4, 2), (8, 9, 9, 5),
                        (6, 8, 7, 7), (4, 5, 0, 1), (8, 10, 1, 8),
                        (3, 5, 8, 10)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 8
        gas = 0
        hitchhickers = [(1, 8, 1, 6)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 8
        gas = 0
        hitchhickers = [(1, 8, 1, 7)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 1

        n_posts = 8
        gas = 0
        hitchhickers = [(1, 8, 1, 8)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 1

        n_posts = 8
        gas = 0
        hitchhickers = [(1, 3, 10, 1), (1, 3, 1, 10), (3, 8, 2, 3)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 3

        n_posts = 8
        gas = 0
        hitchhickers = [(1, 3, 2, 2), (1, 3, 1, 3), (3, 8, 0, 4)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 1

        n_posts = 3
        gas = 0
        hitchhickers = [(1, 2, 1, 1), (2, 3, 1, 1), (1, 3, 1, 2)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 2

        n_posts = 3
        gas = 0
        hitchhickers = [(1, 2, 1, 1), (2, 3, 1, 1), (1, 3, 2, 2)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 2

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 0, 3), (4, 5, 0, 6), (3, 4, 0, 4), (4, 10, 10, 3)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 10

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 0, 3), (4, 5, 11, 6), (3, 4, 0, 4), (4, 10, 10, 3)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 11

        n_posts = 10
        gas = 10
        hitchhickers = [(1, 2, 1000000000, 0), (2, 3, 1000000000, 0), (3, 4, 1000000000, 0),
                        (4, 5, 1000000000, 0), (5, 6, 1000000000, 0), (6, 7, 1000000000, 0),
                        (7, 8, 1000000000, 0), (8, 9, 1000000000, 0), (9, 10, 1000000000, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 9000000000

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 1, 2), (3, 4, 2, 1), (4, 10, 0, 10)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 2

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 3, 2), (3, 4, 2, 1), (4, 10, 0, 10)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 3

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 3, 1), (3, 4, 2, 1), (4, 10, 0, 6)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 3

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 2, 1), (3, 4, 3, 1), (4, 10, 0, 6)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 3

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 2, 1), (3, 4, 3, 1), (4, 10, 0, 5)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 10
        gas = 2
        hitchhickers = [(2, 4, 3, 1), (3, 4, 2, 1), (4, 10, 0, 5)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == -1

        n_posts = 10
        gas = 20
        hitchhickers = [(2, 4, 5, 20), (2, 4, 4, 25), (4, 10, 0, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 5

        n_posts = 10
        gas = 20
        hitchhickers = [(2, 4, 4, 20), (2, 4, 5, 25), (4, 10, 0, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 5

        # edge case avant de lancer la recurrence 
        
        # if maxFuel < n_posts - 1:
        #     return -1
        # elif maxFood == 0 and maxFuel >= n_posts:
        #     return 0

        # capper le gaz au max de posts
        print("All ok")

        exit()


if __name__ == '__main__':

    tests(False)

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