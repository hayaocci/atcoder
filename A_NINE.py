
a_b = input()
a_b = a_b.split()

a = int(a_b[0])
b = int(a_b[1])
c = abs(a-b)

if 1 <= a <= 3 and 1 <= b <= 3:
    if c == 1:
        print("Yes")
    else:
        print("No")
elif 4 <= a <= 6 and 4 <= b <= 6:
    if c == 1:
        print("Yes")
    else:
        print("No")
elif 7 <= a <= 9 and 7 <= b <= 9:

        if c == 1:
            print("Yes")
        else:
            print("No")
else:
    print("No")
