import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

from collections import defaultdict
N, M = map(int, input().split())


en_dict = defaultdict(int)
for _ in range(N):
    s = input().rstrip()
    if len(s) < M: continue
    en_dict[s]+=1
# print(en_dict)
en_dict = dict(sorted(en_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
en_lst = list(en_dict.keys())
for i in en_lst:
    print(i)    