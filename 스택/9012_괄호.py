import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    word = input().rstrip()
    # print(word)
    boul = 0
    is_valid = True
    for s in word:
        if s == "(":
            boul +=1
        else:
            boul -=1
            if boul < 0:
                is_valid = False
                break
    if is_valid and boul == 0:
        print("YES")
    else:
        print("NO")
