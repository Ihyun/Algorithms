# https://www.acmicpc.net/problem/2161

from collections import deque

N = int(input())
queue = deque(range(N, 0, -1))

while queue:
    print(queue.pop(), '', end='')

    if queue:
        queue.appendleft(queue.pop())

