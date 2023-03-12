# 틀림. 다시 풀어봐야함
def dfs(v):
    visited = [0] * (N + 1)                 # 방문행렬
    visited[v] = 1
    stack = []
    location = v                            # 시작점을 현재 위치로

    ans = [v]

    while True:

        for node in range(N + 1):
            if adj_dfs[location][node] == 1 and visited[node] == 0:     # 간선이 있고 방문하지 않았으면

                visited[node] = 1           # 방문체크
                location = node             # 방문 노드를 현재 위치로
                stack.append(node)          # 방문 노드 넣어주기
                ans.append(node)
                break

        else:                               # 브레이크를 만나지 않고 나오면(갈 길이 없으면) 뒤로 돌아가보자
            if stack:
                location = stack.pop()
            else:
                break

    return ans


def bfs(v):

    visited = [0] * (N + 1)             # 방문행렬
    visited[v] = 1
    q = [v]
    ans = [v]

    while q:                            # 큐가 없을 떄까지
        i = q.pop(0)

        for node in adj_bfs[i]:

            if visited[node] == 0:
                q.append(node)
                ans.append(node)
                visited[node] = 1

    return ans


N, M, V = map(int, input().split())

adj_dfs = [[0] * (N + 1) for _ in range(N + 1)]         # 인접행렬
adj_bfs = [[] for _ in range(N + 1)]

for _ in range(M):
    s, t = map(int, input().split())

    adj_dfs[s][t] = 1
    adj_dfs[t][s] = 1

    adj_bfs[s].append(t)
    adj_bfs[t].append(s)

for x in adj_bfs:                       # 정점이 여러 개 인 경우에는 번호가 작은 거 먼저 방문
    x.sort()

print(*dfs(V))
# print(adj_dfs)

print(*bfs(V))
# print(adj_bfs)
