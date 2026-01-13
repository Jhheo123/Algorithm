import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst = sorted(lst)

def can_install(mid): # 예상 거리
    count = 1 # 첫번째 무조건 설치
    last_x = lst[0]
    for x in lst[1:]:
        if x - last_x >= mid:
            count +=1
            last_x = x
            if count >= c:
                return True
    return False


# 거리의 최소/최대
s, e = 1, (lst[-1] - lst[0])
ans = 0 
while (s<=e):
    mid = (s+e)//2 # 거리 예상
    if can_install(mid):
        ans = mid
        s = mid+1
    else:
        e = mid-1
print(ans)