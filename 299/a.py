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
A - Treasure Chest
https://atcoder.jp/contests/abc299/tasks/abc299_a

'''

n = int(input())
s = str(input())

a = s.index('*')

for i in range (n):
    if s[i] == '|':
        i_1 = i
        break

for i in range (i_1+1, n):
    if s[i] == '|':
        i_2 = i
        break

if i_1 < a < i_2:
    print('in')
else:
    print('out')