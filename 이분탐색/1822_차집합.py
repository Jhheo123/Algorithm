import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

na, nb = map(int, input().split()) # A 집합 속하는 원소 개수, B 집합 속하는 원소 개수
a_keys = list(map(int, input().split()))
a_dict = dict.fromkeys(a_keys, 1)
b_keys = set(map(int, input().split()))

# print(f"a_dict: {a_dict}")

for key, value in a_dict.items():
    if key in b_keys:
        a_dict[key]+=1
a_set = []
cnt = 0
for key, value in a_dict.items():
    if value ==1:
        cnt+=1
        a_set.append(key)
a_set.sort()
print(cnt)

if cnt !=0:
    print(*a_set)

