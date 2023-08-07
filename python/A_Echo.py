#20230624
#A - Echo

#文字列の長さ
n = input()

#文字列の入力
#print("文字列を入力してください")
s = input()

#2Nの文字列を出力
i = 0
letter = ""

while i < int(n):
    letter = letter + s[i]*2
    i = i + 1

print(letter)