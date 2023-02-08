import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr2_dic = {}
for i in arr2:
    arr2_dic[i] = 0             # arr2를 기준으로 딕셔너리 생성

for j in arr:                   # 탐색 후 1++
    if j in arr2_dic.keys():
        arr2_dic[j] = 1

print(*arr2_dic.values())


'''시간초과
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

result = [0] * M

for i in range(len(arr2)):
    if arr2[i] in arr:
        result[i] = 1
    else:
        result[i] = 0
        
print(*result)
'''