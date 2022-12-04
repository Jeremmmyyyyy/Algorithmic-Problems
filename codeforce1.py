def getInput(output = False):
    
    n_posts, n_hitch, gas = map(int, input().split())
    hitchhickers = []
    for i in range(0, n_hitch):
        start, end, food, gasol = map(int, input().split())
        hitchhickers.append((start, end, food, gasol))

    if output:
        print(f'{n_posts} {n_hitch} {gas}')
        for i in range(0, n_hitch):
            print(hitchhickers[i])
    
    return n_posts, n_hitch, gas, hitchhickers


def memorized_mad_max_aux(posts, gasAvailable, M, T):
    index = posts - 1
    if M[index] >= 0:
        return M[index]
    
    if posts == 1:
        result = 0
        # for i in range(len(T[index])):
        #     if T[index][i][2] > result:
        #         result = T[index][i][2]
    else:
        result = -1
        
        if len(T[index]) > 0:
            for i in range(len(T[index])):
                if gasAvailable + T[index][i][3]> 0:
                    result = max(
                            result,
                            memorized_mad_max_aux(posts - 1, gasAvailable - 1, M, T),
                            memorized_mad_max_aux(T[index][i][0], gasAvailable - (T[index][i][1] - T[index][i][0]) + T[index][i][3], M, T) + T[index][i][2]
                        )
                else:
                    result = -1
        else:
            if gasAvailable > 0:
                result = memorized_mad_max_aux(posts - 1, gasAvailable - 1, M, T)
            else:
                result = -1

    M[index] = result
    return result


def memorized_mad_max(n_posts, n_hitch, gas, hitchhickers):
    if n_posts == 0:
        return 0
    else:
        m = [-1] * (n_posts)
        newTable = []
        for i in range(n_posts):
            newTable.append([])
        for index, value in enumerate(hitchhickers):
            newTable[value[1] - 1].append(value)
            if value[0] == value [1]:
                return - 1

        return memorized_mad_max_aux(n_posts, gas, m, newTable)

def tests(bool = False):
    if bool:
        n_posts = 3
        n_hitch = 2
        gas = 1
        hitchhickers = [(1, 3, 3, 2), (2, 3, 4, 1)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == 4

        n_posts = 3
        n_hitch = 2
        gas = 0
        hitchhickers = [(1, 2, 3, 0), (2, 3, 4, 0)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == -1

        n_posts = 3
        n_hitch = 3
        gas = 1
        hitchhickers = [(2, 3, 5, 0), (2, 3, 6, 0), (1, 3, 67, 5)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == 67

        n_posts = 1
        n_hitch = 2
        gas = 0
        hitchhickers = [(0, 0, 5, 0), (0, 0, 6, 0)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == -1

        n_posts = 1
        n_hitch = 2
        gas = 0
        hitchhickers = [(1, 1, 5, 0), (1, 1, 6, 0)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == -1

        n_posts = 3
        n_hitch = 1
        gas = 1
        hitchhickers = [(3, 3, 5, 5)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == -1

        n_posts = 3
        n_hitch = 2
        gas = 1
        hitchhickers = [(2, 3, 5, 5), (3, 2, 5, 5)]
        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        assert res == -1

        print("All ok")

        exit()


if __name__ == '__main__':

    tests(True)

    try:
        n_posts, n_hitch, gas, hitchhickers = getInput()
    except:
        print("Impossible")
    else:

        res = memorized_mad_max(n_posts, n_hitch, gas, hitchhickers)
        if res < 0:
            print("Impossible")
        else:
            print(res)