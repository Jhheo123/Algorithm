import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
for _ in range(m):
    lst.append(int(input()))
# print(lst)

s, e = 1, max(lst)
while(s<=e):
    mid = (s+e) // 2
    total = 0
    for k in lst:
        if k % mid == 0:
            total += k//mid
        else:
            total += k//mid+1
    if total <= n:
        e = mid-1
    else:
        s = mid+1
print(s)