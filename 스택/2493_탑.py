import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N = int(input()) # 탑의 수
lst = list(map(int, input().split())) # 탑의 높이

# 정답 담을 리스트
ans = [0]*N
# 신호를 받을 가능성이 있는 정보 넣기
stack = [] #(탑의 인덱스, 탑의 높이)

# 첫번째 탑부터 마지막 탑까지 하나씩 확인 (i: 현재 탑의 번호)
for i in range(N):
    # 스택에 탑이 들어있고, 내 앞에 있는 탑이 나보다 키가 작다면 (높이만 보기)
    while stack and stack[-1][1] <  lst[i]:
        # 내가 더 크니까 내 뒤 신호 못받음. 스택에서 제거하기
        stack.pop()
    
    # 내 신호를 받을 탑
    if stack:
        ans[i] = stack[-1][0] +1
    
    # 나도 스택에 들어가기
    stack.append((i, lst[i]))
print(*(ans))

    