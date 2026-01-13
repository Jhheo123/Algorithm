import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

def func():
    s = 0 # 최소 길이
    e = max(lst) # 최대 길이
    result = 0 # 절단기 설정 최대 높이
    while (s<=e):
        total = 0 # 잘라지는 나무 양
        mid = (s+e)//2
        for x in lst:
            if x > mid:
                total += (x-mid)
        if total < m: # 나무가 부족
            e = mid-1
        else:
            result = mid
            s = mid+1
    return result

print(func())
            

