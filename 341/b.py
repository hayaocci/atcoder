##テンプレコードを書いていく
import heapq
from collections import deque, defaultdict
import math
import sys
import random
sys.setrecursionlimit(1000000)
def map_int(): return map(int, input().split())
def list_int(): return list(map(int, input().split()))
def ii(): return int(input())
def mi():return map(int, input().split())
def lmi(): return list(map(int, input().split()))

n = ii()
a = lmi()

s_list = []
t_list = []

for i in range(n-1):
    num = lmi()
    s_list.append(num[0])
    t_list.append(num[1])

# 処理
i = random.randint(0, n-1)
print(i)
for _ in range(i):
    if a[i] >= s_list[i]:
        a[i] -= s_list[i]
        a[i+1] += t_list[i]

print(max(a))