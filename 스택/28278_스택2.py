import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline
import sys
n = int(input())
stack = []
out = []
for _ in range(n):
    cmd = input().split()
    s = int(cmd[0])
    
    if s == 1:
        stack.append(cmd[1])
    elif s==2:
        out.append(str(stack.pop()) if stack else "-1")
    elif s==3:
        out.append(str(len(stack)))
    elif s==4:
        out.append("0" if stack else "1")
    elif s == 5:
        out.append(str(stack[-1]) if stack else "-1")
sys.stdout.write("\n".join(out))
