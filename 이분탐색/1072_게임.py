import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

x, y = map(int, input().split())
default_z = (y * 100) // x

s, e = 0, 1000000000
cnt = 0
while (s<=e):
    mid = (s+e)//2
    if ((y + mid) * 100) // (x + mid) > default_z:
        cnt = mid
        e = mid-1
    else:
        s = mid+1
if cnt == 0:
    print(-1)
else:
    print(cnt)
