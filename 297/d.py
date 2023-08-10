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

a, b = list(map(int, input().split()))

ans = 0

while True:
    if a == b:
        break
    else:
        if a-b>0:
            if b == 1:
                a = a-b
                ans += 1
            else:
                x = a//b
                a = a - x*b
                ans += x
        elif a-b<0:
            if a == 1:
                b = b-a
                ans += 1
            else:
                y = b//a
                b = b - y*a
                ans += y

print(ans)

# while a != b:
#     if a-b>0:
#         x = (a-b)//b
#         a = a - x*b
#         ans += x
#     elif a-b<0:
#         x = (b-a)//a
#         b = b - x*a
#         ans += x
#     else:
#         break

# print(ans)
    

        



# ans = 0

# if a == b:
#     ans = 0
# else:
#     if a-b>0:
#         ans = (a-b)/b
#     else:
#         ans = (b-a)/a

# print(ans)



# count = 0
# while a != b:

#     if a-b>0:
#         a = a-b
#     elif a-b<0:
#         b = b-a
#     else:
#         break
#     count += 1

# print(count)