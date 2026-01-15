# 투포인터
import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

ans = abs(arr[0]+arr[-1])
p1, p2 = 0, len(arr)-1 # 처음과 마지막 인덱스
ans_lst = [arr[p1], arr[p2]]
while p1 < p2:
    tmp = arr[p1]+arr[p2]
    if abs(tmp)<= ans:
        ans = abs(tmp)
        ans_lst = [arr[p1], arr[p2]]
        if tmp == 0:
            break
    if tmp < 0:
        p1 +=1
    else:
        p2 -=1
print(" ".join(map(str, ans_lst)))

