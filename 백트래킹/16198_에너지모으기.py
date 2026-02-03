import sys
sys.stdin=open("./input.txt","r") # 로컬 테스트용
input = sys.stdin.readline

N = int(input()) # 에너지 구슬의 개수
lst = list(map(int, input().split())) # 에너지 구슬의 무게

ans = 0
def dfs(lst, candi):
    global ans
    if len(lst) == 2:
        ans = max(ans, candi)
        return
    for i in range(1, len(lst)-1):
        add_energe = lst[i-1]*lst[i+1]
        remove_item = lst.pop(i)
        dfs(lst, candi+add_energe)
        lst.insert(i, remove_item)

dfs(lst, 0)
print(ans)