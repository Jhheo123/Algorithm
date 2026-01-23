import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0]*(k+1)
dp[0] = 1
lst = []
for i in range(n):
    lst.append(int(input()))
# print(lst)

for i in lst:
    for j in range(i, k+1):
        dp[j] = dp[j] + dp[j-i]
        # print(dp)
print(dp[k])