def bfs(s):
    global count
    visited = [0] * (C + 1)                 # 방문행렬
    visited[s] = 1                          # 출발지 방문 체크
    q = [s]                                 # 출발지 큐에 넣어줘

    while q:                                # 큐가 바닥 날 떄까지
        t = q.pop(0)

        for i in adj[t]:                    # 인접행렬을 돌아
            if visited[i] == 0:             # 방문하지 않았으면 큐에 넣어주고 방문 체크. count ++
                q.append(i)
                visited[i] = 1
                count += 1

    return count


C = int(input())
N = int(input())

adj = [[] for _ in range(C + 1)]        # 인접행렬

for _ in range(N):
    a, b = map(int, input().split())    # 방향성이 없으므로 양쪽 방향으로 다 만들어줘
    adj[a].append(b)
    adj[b].append(a)

    count = 0

print(bfs(1))
# print(adj)
