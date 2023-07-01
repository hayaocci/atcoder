#python

number1 = input()
number = number1.split()
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(0, 6):
    if number[i] <= number[i+1]:
        count1 +=1

if nuｍber[6] <= number[7]:
    count4 = count4 + 1

for j in range(0, 7):
    if int(number[j]) >= 100 and int(number[j]) <= 675:
        count2 +=1

for x in range (0, 7):
    if int(number[x]) % 25 ==0:
        count3 +=1

if count3 == 7 and count2 == 7 and count1 == 6 and count4 == 1:
    print("Yes")
else:
    print("No")