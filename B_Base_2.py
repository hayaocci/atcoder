#20230623
#B - Base 2

#入力
a = input()



#処理
length = len(a)
i = 0
j = 0
result = 0
while i < length:

    while j < 64:
        result = result + str(a[i])**j

    i = i + 2

#出力
print(result)