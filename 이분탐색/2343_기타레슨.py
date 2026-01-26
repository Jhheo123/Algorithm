import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split()) # 강의 수, 최종 블루레이 개수
lst = list(map(int, input().split()))

start, end = max(lst), sum(lst)
ans = end
while(start<=end):
    mid = (start+end)//2 # 블루레이 길이
    total =0 # 블루레이 길이 담기
    cnt = 1 # 첫번째 블루레이 시작

    for lecture in lst:
        if total+lecture > mid:
            cnt+=1
            total = lecture
        else:
            total+=lecture
    
    if cnt <= m:
        ans = mid
        end = mid-1
    else:
        start = mid+1
print(ans)




