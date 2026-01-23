import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

MAX = 15000
dp = [False]*(MAX+1)
dp[0] = True # 아무것도 안쓰면 무게 0 가능

for w in weights:
    next_dp = dp[:] # 기존 상태 복사
    for i in range(MAX+1):
        if dp[i]: # True인 경우
            # 추를 왼쪽에 올리는 경우
            if i+w <=MAX:
                next_dp[i+w] = True
            # 추를 오른쪽에 올리는 경우
            next_dp[abs(i-w)] = True
    # 다음 dp
    dp = next_dp

ans = []
for t in targets:
    if t <= MAX and dp[t]:
        ans.append("Y")
    else:
        ans.append("N")

print(" ".join(ans))
