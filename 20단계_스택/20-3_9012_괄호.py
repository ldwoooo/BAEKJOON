import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    PS = sys.stdin.readline().strip()

    stack = []
    for i in PS:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else:                               # break를 만나지 않고 for문을 나왔을 경우!!!
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
