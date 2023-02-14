import sys

K = int(sys.stdin.readline().strip())
num = [int(sys.stdin.readline().strip()) for _ in range(K)]
stack = []
for i in num:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))
