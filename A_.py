N =input()
S= input()

a = 0
b = 0
c = 0

for i in range(int(N)):
    s = S[i]

    if s == 'A':
        a += 1
    elif s == 'B':
        b += 1
    elif s == 'C':
        c += 1
    
    if a > 0 and b > 0 and c > 0:
        x = i + 1
        break

print(x)