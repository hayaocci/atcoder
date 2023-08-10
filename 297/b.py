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

s = str(input())

x = s.index('B') +1
y = s.rindex('B') +1
a = s.index('R') +1
b = s.rindex('R') +1
z = s.index('K') +1

if (y-x)%2==1 and a < z < b:
    print('Yes')
else:
    print('No')