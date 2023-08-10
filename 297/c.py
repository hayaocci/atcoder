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

h, w = list(map(int, input().split()))

s = []

for i in range (h):
    s.append(input())

for i in range (h):
    a = list(s[i])
    for j in range (w-1):
        if a[j] == 'T' and a[j+1] == 'T':
            a[j] ='P'
            a[j+1] = 'C'

    print(''.join(a))