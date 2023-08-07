#A - Attack

a_b_input = input()
a_b = a_b_input.split()

a = int(a_b[0])
b = int(a_b[1])
n = 0

while a > 0:
    a = a - b
    n = n + 1

print(n)