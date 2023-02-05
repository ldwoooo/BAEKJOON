import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 중복되는 숫자를 제거하고 인덱스를 활용하기 위해 정렬
clean_arr = sorted(set(arr))
dict = {}

# 인덱스 활용. 딕셔너리 형태로 각 숫자의 인덱스(작은 값의 개수)를 넣어줌
for i in range(len(clean_arr)):
    dict[clean_arr[i]] = i

# dict에서 arr 숫자(Key)에 해당하는 Value 값 출력
for j in arr:
    print(dict[j], end = ' ')

''' 시간초과
N = int(input())
arr = list(map(int, input().split()))
counts = []

for i in range(N):

    a = arr.pop(0)
    count = 0

    for j in set(arr):
        if a > j:
            count += 1

    counts.append(count)
    arr.append(a)

print(counts)
'''
#-----------------------------------------------------------------------
'''
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

a = sorted(set(arr))
counts = []

for i in arr:
    for j in range(len(a)):
        if i == a[j]:
            counts.append(j)
            break

print(*counts)
'''