def push(data):
    stack.append(data)

n = int(input())

num = [int(input()) for _ in range(n)]

stack = []
for i in num:
    for j in range(1, n + 1):
        if j != i:
            stack.append('+')
        else:
            stack.append('+')
            stack.append('-')