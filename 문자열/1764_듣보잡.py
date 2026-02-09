import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

N, M = map(int, input().split())
num_to_name = {}
name_to_num = {}
for i in range(1, N+1):
    s = input().rstrip()
    num_to_name[str(i)] = s
    name_to_num[s] = str(i)


for _ in range(M):
    s = input().rstrip()
    if s.isdigit():
        print(num_to_name[s])
    else:
        print(name_to_num[s])

        
