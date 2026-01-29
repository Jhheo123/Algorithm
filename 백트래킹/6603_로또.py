import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

def dfs(n):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(n, N):
        result.append(lst[i])
        dfs(i+1)
        result.pop()


while (True):
    lst = list(map(int, input().split()))
    
    if len(lst) == 1 and lst[0] == 0:
        break
    N = lst[0]
    lst = sorted(lst[1:])
    # print(lst)
    result = []
    dfs(0)
    print()