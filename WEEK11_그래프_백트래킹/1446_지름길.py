def bfs(s, e):

    q = [s]

    while q:
        t = q.pop(0)

        if t == e:
            break

        if adj[t]:
            q.append(adj[t][0])
            visited[adj[t][0]] = visited[t] + adj[t][1]
        else:
            q.append(t + 1)
            visited[t + 1] = visited[t] + 1


N, D = map(int, input().split())
shortcut = [list(map(int, input().split())) for _ in range(N)]

adj = [[] for _ in range(101)]
for i in range(N):
    ni, nj, d = shortcut[i][0], shortcut[i][1], shortcut[i][2]
    adj[ni].append(nj)
    adj[ni].append(d)

visited = [0] * (D + 1)
bfs(0, D)
print(visited)
