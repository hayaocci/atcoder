'''
https://atcoder.jp/contests/abc313/tasks/abc313_a


'''

import copy

N = input()
P = input()
P = P.split()
P = [int(s) for s in P]

if N == 1:
    print(0)
    exit()

P_one = copy.deepcopy(P[0])

del P[0]

P_max = max(P)

x = P_max - P_one

if x >= 0:
    print(x + 1)
else:
    print(0)

# うまくいかなかったコード
