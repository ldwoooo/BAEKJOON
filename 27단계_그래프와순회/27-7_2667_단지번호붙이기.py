N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

group = 0
ans = []
for i in range(N):                                          # 2차 배열 탐색
    for j in range(N):

        house = 0
        if arr[i][j] == 1:                                  # 집이 있으면
            group += 1                                      # 냅다 단지수와 집의 수 더하기
            house += 1
            s, t = i, j                                     # 집 인덱스 기억하고 큐에 넣어주고
            q = [(s, t)]
            arr[s][t] = 0                                   # 체크한 집은 나중에 다시 돌 때 겹치지 않게 0으로 바꿔줌

            while q:

                a, b = q.pop(0)
                for da, db in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                    na, nb = a + da, b + db
                    if (0 <= na < N) and (0 <= nb < N) and arr[na][nb]:     # 유효한 인덱스이고 집이 있으면
                        house += 1                                          # 냅다 집의 수 더하고 체크한 집 0으로 바꿔주고 큐에 넣어줌
                        arr[na][nb] = 0
                        q.append((na, nb))

            ans.append(house)                               # 한 단지를 다 돌면 집의 수 ans 에 넣어둬

print(group)

ans.sort()                              # 오름차순으로 정렬하고 출력
for i in ans:
    print(i)
