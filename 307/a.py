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
a = list(map(int, input().split()))

week = []

for i in range (n):
    sum_a = sum(a[7*i:7*i+7])
    week.append(sum_a)

print(' '.join(map(str, week)))