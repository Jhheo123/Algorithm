import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

S, P = map(int, input().split())
lst = list(input().rstrip())
# print("lst: ", lst)
value = list(map(int, input().split()))
key = ['A','C','G','T']
dna_dict = dict(zip(key, value))

current_dict = {'A':0, 'C':0, "G":0, "T":0}
count = 0

def check():
    for k in 'ACGT':
        if current_dict[k] < dna_dict[k]:
            return False
    return True

for i in range(P):
    current_dict[lst[i]] +=1

if check():
    count+=1

for i in range(P, S):
    current_dict[lst[i]] +=1
    current_dict[lst[i-P]] -=1

    if check():
        count+=1
print(count)