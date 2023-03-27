def func(n, arr):
    global blue, white

    for c in arr:
        if 0 not in c:
            continue
        blue += 1
        return

    for c in arr:
        if 1 not in c:
            continue
        white += 1
        return

    a1 = []
    a2 = []
    a3 = []
    a4 = []
    for i in range(n):
        left = []
        right = []
        for j in range(n):
            if j <= (n - 1) // 2:
                left.append(paper[i][j])
            else:
                right.append(paper[i][j])

        if i <= (n-1) // 2:
            a1.append(left)
            a2.append(right)
        else:
            a3.append(left)
            a4.append(right)

    func(n // 2, a1)
    func(n // 2, a2)
    func(n // 2, a3)
    func(n // 2, a4)

    return blue, white


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = white = 0
print(paper)
print(func(N, paper))

