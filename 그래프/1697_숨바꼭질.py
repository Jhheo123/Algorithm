import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
MAX = 100001
def bfs(n):
    q = deque([n])
    arr[n] = 0

    while q:
        c = q.popleft()
        if c == k:
            print(arr[c])
            return 
        for dr in (c-1, c+1, 2*c):
            if 0<=dr<MAX and arr[dr] == 0:
                arr[dr] = arr[c] +1
                q.append(dr)

arr = [0]*MAX
bfs(n)