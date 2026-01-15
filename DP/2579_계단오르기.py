import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n = int(input()) # 계단의 개수
lst = [int(input()) for _ in range(n)]
# print(lst)

dp = [0]*n

if len(lst) <=2: # 만약 길이가 2이하라면 다 더한 것이 가장 최댓값
    print(sum(lst))
else: # 아니라면
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])
    print(dp[-1])


