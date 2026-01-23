import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1) # 만들어야하는 금액까지 갈때
    dp[0] = 1
    for i in lst:
        for j in range(i, m+1):
            dp[j] = dp[j] + dp[j-i]
    print(dp[m])