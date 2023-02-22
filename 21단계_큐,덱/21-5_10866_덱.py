from collections import deque
import sys

N = int(sys.stdin.readline().strip())
d = deque()
for _ in range(N):
    txt = sys.stdin.readline().strip()

    if 'push_back' in txt:
        d.append(txt[10:])
    elif 'push_front' in txt:
        d.appendleft(txt[11:])
    elif txt == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif txt == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)
    elif txt == 'size':
        print(len(d))
    elif txt == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif txt == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif txt == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
