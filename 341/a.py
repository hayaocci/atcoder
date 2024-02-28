##テンプレコードを書いていく
import heapq
from collections import deque, defaultdict
import math
import sys
import os
sys.setrecursionlimit(1000000)
def map_int(): return map(int, input().split())
def list_int(): return list(map(int, input().split()))
def ii(): return int(input())
def mi():return map(int, input().split())
def lmi(): return list(map(int, input().split()))


num = int(input())

num_list = []

for i in range(num):
    num_list.append("1")
    num_list.append("0")

num_list.append("1")

print(''.join(num_list))