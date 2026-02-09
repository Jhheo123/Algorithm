import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
current_sum = 0
start = 0
end = 0

while True:
    # 현재 합이 M보다 크거나 같으면 start를 이동시켜 합 줄이기 
    if current_sum >= M:
        current_sum -= nums[start]
        start +=1
    # end가 끝까지 왔으면 루프 종료 
    elif end == N:
        break
    else:
        current_sum += nums[end]
        end +=1
    if current_sum == M:
        count+=1 
print(count)

