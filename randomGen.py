import random
import codeforce3

#original values
posts = 2000
hh = 2000
maxInt = 10**9

#edgecases
# posts = 1000
# hh = 10
# maxInt = 2000

def randomInput():
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


if __name__ == '__main__':
    for i in range(2000):
        n_posts, gas, hitchhickers = randomInput()
        try:
            res = codeforce3.memorized_mad_max(n_posts, gas, hitchhickers)
        except RecursionError:
            print(n_posts, gas)
            print(hitchhickers)
        