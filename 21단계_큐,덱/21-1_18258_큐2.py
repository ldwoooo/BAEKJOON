import sys
from collections import deque

N = int(sys.stdin.readline().strip())

q = deque()
for _ in range(N):
    txt = sys.stdin.readline().strip()

    if 'push' in txt:
        q.append(txt[5:])
    elif txt == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif txt == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif txt == 'size':
        print(len(q))
    elif txt == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif txt == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
