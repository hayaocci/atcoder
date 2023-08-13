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


r = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
r_ = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
ra = list(map(int, str(r_).split()))

print(ra)

n = int(input()) - 2

ans = str(ra[n])

ans = "".join(map(str, ans))

print("3." + ans)



# # a = '{:.' + '0' + str(n) + 'f}'

# # print(a.format(r))

# print(round(r, n))

# import math

# n = int(input())  # 切り捨てしたい桁
# # x = 1.555
# y = math.floor(r * 10 ** n) / (10 ** n)


