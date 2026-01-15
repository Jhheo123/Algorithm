import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 정렬 / set
sorted_lst = sorted(set(lst))

def search(item):
    s, e = 0, len(sorted_lst)-1
    while(s<=e):
        mid = (s+e)//2
        if item == sorted_lst[mid]:
            return mid
        elif item < sorted_lst[mid]:
            e = mid-1
        else:
            s = mid+1

# print(sorted_lst)
ans = []
for item in lst:
    ans.append(search(item))
print(" ".join(map(str, ans)))