import sys

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []                  # 1~n까지 숫자들을 쌓을 리스트
top = -1                    # stack 의 인덱스
result = []                 # 결과값을 넣을 리스트
j = 0

for i in range(1, n + 1):

    # 1을 넣어주며 시작
    stack.append(i)
    result.append('+')
    top += 1

    while True:

        # arr 리스트를 다 돌거나 stack 이 비어있으면 break
        if j == n or top == -1:
            break

        # stack 의 마지막 값과 arr 의 값이 같지 않으면 다시 넣어주러 가
        elif stack[top] != arr[j]:
            break

        # stack 의 마지막 값과 arr 의 값이 같으면
        else:
            # 해당 값 빼주고 인덱스 감소, arr 인덱스(j) 증가
            stack.pop()
            result.append('-')
            top -= 1
            j += 1

# 1~n까지 다 돌았는데 stack 이 남아있으면 불가능
if len(stack) != 0:
    print('NO')
else:
    print('\n'.join(result))

# -----------------------------------------------------------------------
# 백준 가장 빠른 코드
# import sys
#
#
# def solution():
#     n, *nums = map(int, sys.stdin.buffer.read().splitlines())
#     s = []
#     answer = []
#     cur = 1
#     for value in nums:
#         while cur <= value:
#             answer.append('+')
#             s.append(cur)
#             cur += 1
#         if s.pop() != value:
#             return "NO"
#         answer.append('-')
#     return '\n'.join(answer)
#
#
# print(solution())