N, K = map(int, input().split())

visited = [0] * 100001
visited[N] = 0
q = [N]
while True:                         # bfs, 누적합. 점점 퍼져나감
    a = q.pop(0)

    if a == K:
        break

    if a - 1 >= 0 and visited[a - 1] == 0:      # 뒤로 갔을 떄
        visited[a - 1] = visited[a] + 1
        q.append(a - 1)

    if a + 1 < 100001 and visited[a + 1] == 0:  # 앞으로 갔을 떄
        visited[a + 1] = visited[a] + 1
        q.append(a + 1)

    if a * 2 < 100001 and visited[a * 2] == 0:  # 순간이동 했을 떄
        visited[a * 2] = visited[a] + 1
        q.append(a * 2)

print(visited[K])
