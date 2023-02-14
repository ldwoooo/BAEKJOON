import sys

N = int(sys.stdin.readline().strip())
order = [sys.stdin.readline().strip() for _ in range(N)]
stack = []
for i in order:
    if i == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            x = stack.pop()
            print(x)

    elif i == 'size':
        print(len(stack))

    elif i == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif i == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    else:
        num = int(i[4:])
        stack.append(num)
