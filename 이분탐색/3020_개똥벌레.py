import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

# n: 장애물 개수 (짝수)
# h: 동굴 높이 
# 짝수 번째: 아래에서 자라는 석순
# 홀수 번째: 위에서 내려오는 종유석

n, h = map(int, input().split())
down = [0] * (h+1) # 높이 k 인 석순 개수
up = [0] * (h+1) # 높이 k 인 종유석 개수

for i in range(n):
    k = int(input())
    if i%2 == 0:
        down[k] +=1
    else:
        up[k] +=1
# print(up, down)

for i in range(h-1, 0, -1):
    down[i] += down[i+1] # 높이 i 이상인 석순 개수

for i in range(h-1, 0, -1):
    up[i] += up[i+1] # 길이 i 이상인 종유석 개수
# print(up, down) # 

result = n
num = 0

for i in range(1, h+1):
    cnt = down[i] + up[h-i+1]

    if cnt < result:
        result = cnt
        num = 1
    elif cnt == result:
        num +=1
print(result, num)