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

n, d = map(int, input().split())
t = list(map(int, input().split()))
a = 0

for i in range (n-1):
    if t[i+1]-t[i] <= d:
        print(t[i+1])
        a = 1
        break

if a == 0:
    print(-1)