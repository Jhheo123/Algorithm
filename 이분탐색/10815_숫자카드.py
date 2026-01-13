import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n = int(input()) # 상근이가 가지고 있는 숫자 개수
arr = sorted(list(map(int, input().split())))
m = int(input()) # 상근이가 가지고 있는건지 아닌지 확인
lst = list(map(int, input().split()))
# print(arr)
def func(a):
    six, eix = 0, len(arr)-1 # index 
    while (six <= eix):
        
        mid = (six + eix) // 2 # 중간 인덱스부터 탐색
        if a < arr[mid]:
            eix = mid-1
        elif a>arr[mid]:
            six = mid+1
        else:
            return 1
    return 0

# 상근이가 가지고있으면 1, 아니면 0
ans = []
for a in lst:
    ans.append(func(a))
print(" ".join(map(str, ans)))
