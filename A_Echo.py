#20230624
#A - Echo

#文字列の入力
print("文字列を入力してください")
n = input()

#入力した文字列の確認
print("入力した文字列は" + n)

#文字列の長さ
s = len(n)
print("文字列の長さは" + str(s))

o = list(n)
print(o)

o1 = list(list_split(o, 1))
print(o1)

'''
i = 0
while i < s:
    output= n[i] + n[i]
    print(output1)

    i = i + 1
'''