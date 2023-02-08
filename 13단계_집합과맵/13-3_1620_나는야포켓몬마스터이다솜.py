import sys

N, M = map(int, sys.stdin.readline().strip().split())

pocketmon_name = {sys.stdin.readline().strip() : str(i) for i in range(1, N + 1)}
pocketmon_num = {str(i) : sys.stdin.readline().strip() for i in range(1, N + 1)}

print(pocketmon_name)
print(pocketmon_num)

# import sys

# N, M = map(int, sys.stdin.readline().strip().split())

# pocketmon_dict = {sys.stdin.readline().strip() : str(i) for i in range(1, N + 1)}

# # 아래와 같은 의미
# # pocketmon_dict = {}

# # for i in range(N):
# #     name = input()
# #     pocketmon_dict[name] = i + 1

# quiz = [sys.stdin.readline().strip() for _ in range(M)]

# for j in quiz:
#     for name, num in pocketmon_dict.items():
#         if j == name:
#             print(num)
#         elif j == num:
#             print(name)