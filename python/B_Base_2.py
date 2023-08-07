#20230623
#B - Base 2

#入力
a = input()

#処理
length = len(a)

#スペースの消去
i = 0
input_number =""
while i < length:
    input_number = input_number + a[i]
    i = i + 2

#結果の計算
j = 0
result = 0
input_number_length = len(input_number)

while j < input_number_length:
    result = result + int(input_number[j])*(2**j)
    j = j + 1

#出力
print(result)