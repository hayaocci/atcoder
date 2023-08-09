'''
A - N-choice question 
https://atcoder.jp/contests/abc300/tasks/abc300_a

'''

nab = list(map(int, input().split()))
C_all = list(map(int, input().split()))

n = nab[0]
a = nab[1]
b = nab[2]
t = a + b

for i in range(n):
    c = C_all[i]
    
    if c == t:
        print(i+1)
        break

'''
別解

配列の検索にindexを使う
https://www.youtube.com/watch?v=P7CL5TfLqCM

'''
