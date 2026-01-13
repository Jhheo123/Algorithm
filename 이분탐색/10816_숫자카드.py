import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline



n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
m = int(input())
arr = list(map(int, input().split()))


def lower_bound(a,x):
    """
    x 이상이 처음 등장하는 위치를 찾는 함수
    (즉, x가 시작되는 인덱스)
    """
    s, e = 0, len(a)
    # 탐색 구간이 남아 있는 동안 반복
    while s<e:
        mid = (s+e)//2
        # mid 위치 값이 x이상이면, x는 mid 포함 왼쪽에 있을 수 있음
        if a[mid] >= x:
            e = mid
        else:
            # mid 값이 x보다 작으면 x는 mid 오른쪽에 있음
            s = mid+1
    # s==e가 되는 지점이 x가 처음 등장하는 위치
    return s

def upper_bound(a, x):
    """
    x보다 큰 값이 처음 등장하는 위치를 찾는 함수
    (즉, x가 끝나는 다음 인덱스)
    """
    s, e = 0, len(a)
    while s < e:
        mid = (s+e)//2
        # mid 위치의 값이 x보다 크면
        # 경계를 왼쪽으로 이동
        if a[mid] > x:
            e = mid
        else:
            # mid 값이 x 이하이면
            # x보다 큰 값은 오른쪽에 있음
            s = mid+1
    return s


out = []
for x in arr:
    # (x보다 큰 값의 첫 위치) - (x가 처음 등장하는 위치)
    out.append(str(upper_bound(lst, x) - lower_bound(lst, x)))
print(" ".join(out))
