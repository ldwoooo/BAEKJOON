# 세트 풀이
import sys

N, M = map(int, sys.stdin.readline().strip().split())
never_heard = set(sys.stdin.readline().strip() for _ in range(N))
never_seen = set(sys.stdin.readline().strip() for _ in range(M))

never_heard_seen = [i for i in never_seen if i in never_heard]
''' 같은 의미
non_heard_seem_name = []
for i in never_seen:                     # 보지도 못한 이름들이 듣지도 못한 이름 세트에 있으면 듣보잡 리스트에 넣기.
    if i in never_heard:
        never_heard_seen.append(i)
'''

never_heard_seen.sort()
print(len(never_heard_seen))
print('\n'.join(never_heard_seen)) 

# ----------------------------------------------------------------------
# 리스트 풀이. 시간초과
# import sys
#
# N, M = map(int, sys.stdin.readline().strip().split())
# never_heard = [sys.stdin.readline().strip() for _ in range(N)]
# never_seen = [sys.stdin.readline().strip() for _ in range(M)]
#
# never_heard_seen = [i for i in never_seen if i in never_heard]
#
# print(len(never_heard_seen))
# print('\n'.join(never_heard_seen))

# ----------------------------------------------------------------------
# 딕셔너리 풀이.
import sys

N, M = map(int, sys.stdin.readline().strip().split())
never_heard_seen_name = [sys.stdin.readline().strip() for _ in range(N + M)]

nhs_dict = {}
for i in never_heard_seen_name:             # 딕셔너리 이름을 키값으로 없으면 1로
    if i not in nhs_dict:
        nhs_dict[i] = 1
    else:                                   # 있으면 +1
        nhs_dict[i] += 1

count = 0
nhs_list = []
for name, v in nhs_dict.items():
    if v == 2:                              # 딕셔너리의 value 값이 2인 경우 카운팅.
        count += 1
        nhs_list.append(name)               # 듣보잡 리스트에 해당 이름 넣기.

nhs_list.sort()
print(count)
print('\n'.join(nhs_list))