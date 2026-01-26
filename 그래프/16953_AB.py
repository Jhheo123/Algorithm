import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import deque
a, b = map(int, input().split())

def bfs(a, b):
    q = deque([(a, 1)]) # (현재값, 연산횟수)
    visited = set()
    visited.add(a)

    while q:
        curr, count = q.popleft()
        if curr == b:
            return count
        
        for next in (curr*2, int(str(curr)+'1')):
            if next<=b and next not in visited:
                visited.add(next)
                q.append((next, count+1))
    return -1

print(bfs(a,b))




"""
from collections import deque
a, b = map(int, input().split())
# MAX = 10**9+1
dp = [0]*(b+1)

visited = [0]*(b+1)
def bfs(a):
    q = deque([a])
    visited[a] = 1
    while q:
        c = q.popleft()
        if c == b:
            return visited[c]
        for next in (c*2, int(str(c)+'1')):
            if 1<=next<(b+1) and visited[next] == 0:
                visited[next] = visited[c]+1
                q.append(next)
                # print(q)
    return -1
print(bfs(a))
"""
