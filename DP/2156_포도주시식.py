import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))
# print(lst)

dp = [0] * (n+1)

dp[1] = lst[1]
if n>=2:
    dp[2] = lst[1]+lst[2]

# 3번째 잔부터 점화식
for i in range(3, n+1):
    dp[i] = max(
        dp[i-1],
        dp[i-2] + lst[i],
        dp[i-3] + lst[i-1] + lst[i]
    )

print(dp[n])
