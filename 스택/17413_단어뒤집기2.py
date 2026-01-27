import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

import re
data = input()
# <태그> | [공백] | [일반 단어]
# <[^>]*> : '<'로 시작해서 '>'가 아닌 문자들이 있고 '>'로 끝나는 덩어리 (태그)
# |       : 또는
# [^\s<>]+ : 공백, <, > 가 아닌 문자들이 이어진 덩어리 (일반 단어)
pattern = r'<[^>]*>|\s+|[^\s<>]+'
stack = re.findall(pattern, data)
# print(stack)
ans = []
for word in stack:
    if word.startswith('<'):
        ans.append(word)
    elif word.isspace(): # 공백인 경우
        ans.append(word)
    else:
        ans.append(word[::-1])

print("".join(ans))