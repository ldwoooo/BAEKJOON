N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]                           # 방문행렬
visited[0][0] = 1
q = [(0, 0)]

while q:
    i, j = q.pop(0)

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        # 미로 안에 있고 방문하지 않았고 길이 있다면
        if (0 <= ni < N) and (0 <= nj < M) and (visited[ni][nj] == 0) and maze[ni][nj]:
            q.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1                 # 누적합으로 최단거리 구하기

print(visited[N - 1][M - 1])
