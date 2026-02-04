import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline


N = int(input())
buildings = list(int(input()) for _ in range(N))
# print(stack)
ans = 0
stack = []
for h in buildings:
    # 스택에 있는 빌링 중 현재 빌링 보다 낮거나 같다면 
    # 현재 빌링 때문에 뒤를 볼 수 없으므로 스택에서 제거
    while stack and stack[-1] <= h:
        stack.pop()
    ans += len(stack)
    stack.append(h) # 후보 넣기

print(ans)