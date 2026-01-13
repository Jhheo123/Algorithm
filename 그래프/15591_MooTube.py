# 백준 15591 MooTube 골드 5
import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline
# deque 사용
from collections import deque

t = int(input())


for _ in range(t):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        q.append((i, lst[i])) # (원래 위치, 중요도)
    cnt = 0
    while q:
        cur = q.popleft()
        # 뒤에 더 높은 중요도가 있으면 다시 넣기
        if any(cur[1] < x[1] for x in q):
            q.append(cur)
            # print("q", q)
        else:
            cnt +=1
            # print("cnt", cnt)
            if cur[0] == M:
                print(cnt)
                break