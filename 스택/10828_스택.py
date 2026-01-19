import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    lst= list(input().split())
    # print(lst)
    if len(lst) == 2:
        s, num = lst[0], lst[1]
        num = int(num)
    else:
        s = lst[0]

    if s=='push':
        stack.append(num)
    elif s=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif s=='size':
        print(len(stack))
    elif s == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
