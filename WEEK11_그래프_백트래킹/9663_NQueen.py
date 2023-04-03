def promising(i, j, X, Y):
    for k in range(len(X)):
        if j == X[k] or abs(Y[k] - i) == abs(X[k] - j):
            return 0
    return 1


def f(i, n):
    global cnt
    if i == n:
        cnt += 1
        return

    for j in range(n):
        if promising(i, j, X, Y):
            X.append(j)
            Y.append(i)
            board[i][j] = 1
            f(i + 1, n)
            board[i][j] = 0
            X.pop()
            Y.pop()


X = []
Y = []
N = int(input())
cnt = 0
board = [[0] * N for _ in range(N)]
f(0, N)
print(cnt)
