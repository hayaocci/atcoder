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



n = int(input())
s = str(input())
# s = list(map(int, input().split()))

if 'o' in s:
    pass
else:
    print(-1)
    exit()

l = 0
list = []

for i in range(n):
    if s[i] == 'o':
        l +=1

    else:
        list.append(l)
        l = 0

max_l = max(list)

print(max_l)
