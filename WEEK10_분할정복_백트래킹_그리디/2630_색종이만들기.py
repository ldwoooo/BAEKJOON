def check(arr):                     # 색종이를 판단하는 함수
    for i in range(len(arr)):       # 2차배열에서 한줄씩 돌면서
        if 0 in arr[i]:             # 해당 줄에 0이 들어있으면 멈춰
            break
    else:                           # break를 안만나고 나왔다면 == 0이 모든 줄에 없다
        return 1

    for i in range(len(arr)):
        if 1 in arr[i]:             # 1이 들어있으면 멈춰
            break
    else:                           # 1이 모든 줄에 없으므로 0 반환
        return 0


def f(arr):
    global blue, white

    if len(arr) == 1:               # 색종이가 1블록이고
        if arr[0][0] == 1:          # 그 숫자가 1이면 파란색
            blue += 1
        else:                       # 0이면 흰색
            white += 1
        return

    if check(arr) == 1:             # 판단 함수에서 1로 나오면 파란 종이
        blue += 1
    elif check(arr) == 0:           # 0이 나오면 흰 종이
        white += 1
    else:
        m = len(arr) // 2
        a1 = [[0] * m for _ in range(m)]        # 4분면으로 나눠줌
        a2 = [[0] * m for _ in range(m)]
        a3 = [[0] * m for _ in range(m)]
        a4 = [[0] * m for _ in range(m)]
        for i in range(len(arr)):               # 2차배열 탐색
            for j in range(len(arr)):
                if (i < m) and (j < m):         # 1사분면
                    a1[i][j] = arr[i][j]
                elif (i < m) and (j >= m):      # 2사분면
                    a2[i][j-m] = arr[i][j]
                elif (i >= m) and (j < m):      # 3사분면
                    a3[i-m][j] = arr[i][j]
                elif (i >= m) and (j >= m):     # 4사분면
                    a4[i-m][j-m] = arr[i][j]
        f(a1)
        f(a2)
        f(a3)
        f(a4)
    return


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = white = 0
f(paper)
print(white)
print(blue)
