import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

import heapq
from collections import deque
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost<distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    print(distance[D])

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append((i+1, 1))
for _ in range(N):
    start, end, cost = map(int, input().split())
    if end > D: continue
    graph[start].append((end, cost))
distance = [INF]*(D+1)
dijkstra(0) # 거리 0부터 시작