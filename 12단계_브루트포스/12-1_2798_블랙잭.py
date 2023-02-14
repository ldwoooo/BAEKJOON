import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
result = []

maxV = 0
for i in range(N-2):                            # 3장 뽑으니까 끝에서 3번째 카드까지만 보면 돼.
    for j in range(i+1, N-1):                   # i 다음부터 끝에서 2번째 카드 까지만.
        for k in range(j+1, N):                 # j 다음부터 끝까지.
            sum = nums[i] + nums[j] + nums[k]   # 각 자리 숫자 합.
            if sum <= M:
                result.append(sum)              # M보다 작거나 같은 합들 중 가장 큰 값 출력.
print(max(result))
''' 같은 의미
            if sum <= M:
                if maxV < sum:
                    maxV = sum

print(maxV)
'''

# 비트연산자 풀이. 시간초과
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
for i in range(1,1<<len(numbers)):
    result = []
    for j in range(len(numbers)):
        if i & (1<<j):
            result.append(numbers[j])
    if len(result) != 3:
        continue
        # result의 합이 answer보다 크고 m보다 작으면 answer = sum(result)
        # 아니면 answer = answer
    answer = sum(result) if sum(result) > answer and sum(result) <= m else answer
print(answer)

# 부분집합을 만들때 애초에 3개의 조합만 만들도록 하고 거기서 확인
from itertools import combinations
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
for number in list(combinations(numbers, 3)):
    check = sum(number)
    if sum(number) <= m and check > answer:
        answer = check
print(answer)
