import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split())
m_lst = [0] + list(map(int, input().split()))
c_lst = [0] + list(map(int, input().split()))
max_cost = sum(c_lst)
dp = [[0]*(max_cost+1) for _ in range(n+1)]
ans = max_cost
for i in range(1, n+1):
    for j in range(0, max_cost+1):
        dp[i][j] = dp[i-1][j]
        if c_lst[i] <= j: # 앱을 끌 수 있다면
            dp[i][j] = max(dp[i][j], dp[i-1][j-c_lst[i]] + m_lst[i])

        if dp[i][j] >= m:
            ans = min(ans, j)
print(ans)