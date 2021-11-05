# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())

arr = [0]
i = 0

while len(arr) < 1000:
    i += 1
    for j in range(i):
        arr.append(arr[-1]+i)

print(arr[b]-arr[a-1])
