import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst = sorted(lst)
# print(lst)

# 두 수의 합을 모두 구해서 집합에 넣기
two_sum = set()
for x in lst:
    for y in lst:
        two_sum.add(x+y)


# k-z가 twp_sum 에 존재하는지 확인
ans = -1
for i in range(N-1, -1, -1):
    for j in range(i):
        if (lst[i] - lst[j]) in two_sum:
            ans = lst[i]
            break
    if ans!= -1:
        break
print(ans)