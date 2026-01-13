import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline
# 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
k, n = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))
# print(lst)
# n개의 랜선을 만들고 싶어 잘라서
def func():
    s = 1
    e = max(lst)
    result = 0 # n개의 랜선을 만들때 길이
    while (s<=e):
        total = 0 # 잘려지는 랜선 수
        mid = (s+e)//2
        for x in lst:
            total += x // mid
        if total < n: # 만들고 싶어하는 개수보다 작다면
            e = mid-1
        elif total >= n: # 크다면
            s = mid+1
            result = mid
    return result
print(func())