a, b = list(map(int, input().split()))

ans = 0

while a != b:
    if a-b>0:
        x = (a-b)//b
        a = a - x*b
        ans += x
    elif a-b<0:
        x = (b-a)//a
        b = b - x*a
        ans += x
    else:
        break
    
print(ans)