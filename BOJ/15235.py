# https://www.acmicpc.net/problem/15235

N = int(input())
slices = [*map(int, input().split())]
queue = []
while sum(slices):
    for i, v in enumerate(slices):
        if v > 0:
            queue.append(i+1)
            slices[i] -= 1

que = ''.join(map(chr, queue))

for i in range(1, N+1):
    print(que.rfind(chr(i))+1, '', end='')

