import sys


def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data


def dequeue():
    global front
    front += 2
    return queue[front]


num = int(sys.stdin.readline().strip())

queue = [i for i in range(1, num + 1)] + [0] * 10000000
front = -1
rear = num - 1

while front != rear:
    enqueue(dequeue())

print(queue[rear - 1])

