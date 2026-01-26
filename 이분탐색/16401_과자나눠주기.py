import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline


n, m = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 1, max(lst)
ans = 0
while(start<=end):
    mid = (start + end)//2
    cnt = 0

    for snack in lst:
        cnt+= snack//mid
        
    
    if cnt >= n: # 조카 수보다 많이 혹은 딱 맞춰 만들 수 있다면
        start = mid+1
        ans = mid
    else: # 부족하다면
        end = mid-1
print(ans)