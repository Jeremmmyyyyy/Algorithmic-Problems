import random
from colorama import Fore
from colorama import Style
from codeforce_problem_A import memorized_mad_max
import sys
import traceback


#original values
posts = 2000
hh = 2000
maxInt = 10**9

#edgecases
postsT = 1000
hhT = 10
maxIntT = 2000

def randomInputNormal():
    list = []
    n = random.randint(2, posts)
    m = random.randint(2, hh)
    f = random.randint(0, maxInt)

    for i in range(m):
        ai = random.randint(1, n -1)
        bi = random.randint(ai, n)
        ci = random.randint(0, maxInt)
        fi = random.randint(0, maxInt)

        list.append((ai, bi, ci, fi))

    return n, f, list

def randomInputTuned():
    list = []
    n = random.randint(2, postsT)
    m = random.randint(2, hhT)
    f = random.randint(0, maxIntT)

    for i in range(m):
        ai = random.randint(1, n -1)
        bi = random.randint(ai, n)
        ci = random.randint(0, maxIntT)
        fi = random.randint(0, maxIntT)

        list.append((ai, bi, ci, fi))

    return n, f, list

def randomTesting(normal = True):    
    for i in range(2000):
        if normal:
            n_posts, gas, hitchhickers = randomInputNormal()
        else:
            n_posts, gas, hitchhickers = randomInputTuned()
        try:
            memorized_mad_max(n_posts, gas, hitchhickers)
            
        except RecursionError:
            print(n_posts, gas)
            print(hitchhickers)
            print(f"{Fore.RED}FAIL{Style.RESET_ALL} : For random")
            exit()
    if normal:
        print(f"{Fore.LIGHTGREEN_EX}OK{Style.RESET_ALL} :   For all normal random")
    else:
        print(f"{Fore.LIGHTGREEN_EX}OK{Style.RESET_ALL} :   For all tuned random")

def maxRecDepth1():
    list = []
    for i in range(1200):
        list.append((i + 1, i + 2, 1, 1))
    try:
        res = memorized_mad_max(2000, 2000, list)
    except RecursionError:
        print(f"{Fore.RED}FAIL{Style.RESET_ALL} : For max recursion depth limit 1 ")
        print(traceback.format_exc())
    else:
        assert res == 1200
        print(f"{Fore.LIGHTGREEN_EX}OK{Style.RESET_ALL} :   For max recursion depth limit 1 ")



def maxRecDepth2():
    list = []
    for i in range(1200):
        list.append((1, 10 + i, 1, 1))
    try:
        res = memorized_mad_max(2000, 2000, list)
    except RecursionError:
        print(f"{Fore.RED}FAIL{Style.RESET_ALL} : For max recursion depth limit 2 ")
    else:
        assert res == 1
        print(f"{Fore.LIGHTGREEN_EX}OK{Style.RESET_ALL} :   For max recursion depth limit 2 ")

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

        n_posts = 4
        gas = 10
        hitchhickers = [(1, 2, 1, 10), (1, 2, 2, 10), (2, 4, 3, 10), (2, 4, 4, 10)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 6


        n_posts = 1500
        gas = 1999
        hitchhickers = [(1, 2, 1, 0)]
        res = memorized_mad_max(n_posts, gas, hitchhickers)
        assert res == 1
        
        print(f"{Fore.LIGHTGREEN_EX}OK{Style.RESET_ALL} :   For all normal edgecases")


        


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    tests(True)
    randomTesting(True)
    randomTesting(False)
    maxRecDepth1()
    maxRecDepth2()

    
        