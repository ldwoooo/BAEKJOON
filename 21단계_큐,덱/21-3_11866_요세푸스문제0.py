# deque 이용
import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().strip().split()))

q = deque()
for i in range(1, N + 1):               # 1 ~ N 까지 배열 생성
    q.append(i)

result = deque()
while q:                                # q가 빌 때까지,
    for _ in range(K - 1):              # 제거할 사람들의 간격은 K - 1
        q.append(q.popleft())           # 제거 안 할 사람들은 뒤로 넣고 제거할 사람 맨 앞으로 위치시킨다

    result.append(q.popleft())          # 제거할 사람 제거하고 결과 배열에 넣기

print('<', end = '')                    # 출력 맞춰주기
print(*result, sep = ', ', end = '')
print('>')
# -----------------------------------------------------------------------------------------------
# 선형 큐
import sys

N, K = map(int, sys.stdin.readline().strip().split())

arr = [i for i in range(1, N + 1)]

queue = [0] * 1000000                   # 십만으로 했을 때, 런타임에러
front = rear = -1

for i in range(N):
    rear += 1
    queue[rear] = arr[i]                # queue에 arr 숫자 차례대로 넣어주기

end = -1                                # 결과값 넣어줄 인덱스 및 큐
result_q = [0] * N
while front != rear:                    # 끝나는 조건. front와 rear가 같아질 때 까지

    for _ in range(K - 1):              # 제거할 사람의 간격(K - 1)만큼 반복
        front += 1
        a = queue[front]                # 제거하지 않는 사람 a

        rear += 1
        queue[rear] = a                 # 제거하지 않을 사람 뒤로 넣어줌

    front += 1
    b = queue[front]                    # 제거할 사람(b)이 맨 앞으로 오면
    
    end += 1        
    result_q[end] = b                   # 결과큐에 넣어줌

print('<', end = '')                    # 출력 맞춰주기
print(*result_q, sep = ', ', end = '')
print('>')
