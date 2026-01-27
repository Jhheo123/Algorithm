import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

left_stack = list(map(str, input().rstrip())) # 커서의 왼쪽
# print(left_stack)

right_stack = [] # 커서의 오른쪽

n = int(input())

for _ in range(n):
    lst = list(map(str, input().rstrip().split()))
    # print(lst)

    if lst[0] == 'L': # 커서 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())
    elif lst[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif lst[0] == 'B':
        if left_stack:
            # 커서 왼쪽 글자 삭제
            left_stack.pop()
            
    else: # lst[0] == 'P'
        left_stack.append(lst[1])
        
print("".join(left_stack+right_stack[::-1]))