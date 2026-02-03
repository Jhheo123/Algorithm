import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline


from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# print(graph)

# 다리 정보
max_weight = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    max_weight = max(max_weight, c) # 이분 탐색의 high 로 사용
# print(graph)

# 공장 위치
s, e = map(int, input().split())
# print(s,e) 

def can_go(target_weight):
    "target weight 무게의 트럭이 s에서 e까지 갈 수 있는지 검사"

    q = deque([s,])
    visited = [False]*(N+1)
    visited[s] = True
    while q:
        current = q.popleft()
        if current == e:
            return True
        
        for next_node, next_weight in graph[current]:
            if not visited[next_node] and target_weight <= next_weight:
                q.append(next_node)
                visited[next_node] = True
    return False

# 이분탐색 시작 
low, high = 1, max_weight
ans = 0

while low<=high:
    mid = (low+high) // 2
    if can_go(mid): # 통과 가능한 무게인가?
        ans = mid
        low = mid+1
    else: # 통과 불가능한 무게인가?
        high = mid-1
print(ans)
