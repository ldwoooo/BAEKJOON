# 딕셔너리를 이용하면 탐색속도를 줄일 수 있다
# 탐색해야할 자료수가 많으면 딕셔너리 활용하자!!!!
import sys

N, M = map(int, sys.stdin.readline().split())       # N, M은 변수로 사용할 일이 없으므로 list로 바꿔줄 필요 없음
N_arr = [sys.stdin.readline() for _ in range(N)]
S_arr = [sys.stdin.readline() for _ in range(M)]

N_dict = {}
count = 0

for i in N_arr:
    N_dict[i] = 0               # 딕셔너리 생성

for j in S_arr:
    if j in N_dict.keys():      # key로 있는지 없는지 여부 판단!!
        count += 1
print(count)

'''시간초과
import sys

N, M = map(int, sys.stdin.readline().split())

N_arr = [sys.stdin.readline() for _ in range(N)]
S_arr = [sys.stdin.readline() for _ in range(M)]

count = 0
for i in N_arr:
    for j in S_arr:
        if i == j:
            count += 1
print(count)
'''