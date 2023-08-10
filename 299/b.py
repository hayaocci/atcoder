##テンプレコードを書いていく
import heapq
from collections import deque, defaultdict
import math
import sys
sys.setrecursionlimit(1000000)
def map_int(): return map(int, input().split())
def list_int(): return list(map(int, input().split()))
def ii(): return int(input())
def mi():return map(int, input().split())
def lmi(): return list(map(int, input().split()))

'''
B - Trick Taking 
https://atcoder.jp/contests/abc299/tasks/abc299_b
'''

n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

array_r = []
array_i = []
array_x =[]
array_y = []

for i in range(n):
    if c[i] == t:
        array_r.append(r[i])
        array_i.append(i+1)

if len(array_r) != 0:
    r_max = array_r.index(max(array_r))
    i_num = array_i[r_max]
    print(i_num)
else:
    base_color = c[0]
    for i in range(n):
        if c[i] == base_color:
            array_x.append(r[i])
            array_y.append(i+1)
    x_max = array_x.index(max(array_x))
    y_num = array_y[x_max]

    print(y_num)