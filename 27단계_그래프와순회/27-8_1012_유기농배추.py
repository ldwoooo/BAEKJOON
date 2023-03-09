T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]            # 땅 죄다 0으로 만들어 놓고

    for _ in range(K):                              # 배추 심기
        j, i = map(int, input().split())            # 순서 주의!!!!
        ground[i][j] = 1

    bug = 0                                         # 벌레
    for i in range(N):                              # 땅을 돌아보자
        for j in range(M):
            if ground[i][j]:                        # 배추가 심어져 있으면
                bug += 1                            # 냅다 벌레 더해
                a, b = i, j                         # 땅 계속 돌아야하니까 i,j 기억해 놓고
                q = [(a, b)]
                ground[a][b] = 0                    # 다시 땅을 돌 때 무시할 수 있게 체크한 배추 0으로 만들어주고

                while q:
                    a, b = q.pop(0)
                    for da, db in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        na, nb = a + da, b + db
                        if (0 <= na < N) and (0 <= nb < M) and ground[na][nb]:      # 땅 안, 근처에 배추가 있으면
                            q.append((na, nb))                                      # 새배추 위치 큐에 넣어주고 0으로 만들어
                            ground[na][nb] = 0

    print(bug)
