import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n = int(input())
one_lst = list(map(int, input().split()))
happy_lst = list(map(int, input().split()))

arr = [[0]*100 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if one_lst[i-1] <= j:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-one_lst[i-1]]+ happy_lst[i-1])
        else:
            arr[i][j] = arr[i-1][j]

print(arr[n][99])
