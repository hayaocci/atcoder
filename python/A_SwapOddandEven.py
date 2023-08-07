#A - Swap Odd and Even

s = input()
s_length = len(s)/2
s_output = []

for i in range(1, int(s_length)+1):
    s_output.append(s[2*i-1])
    s_output.append(s[2*i-2])

print("".join(s_output))
