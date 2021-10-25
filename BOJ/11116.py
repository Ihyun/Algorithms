# https://www.acmicpc.net/problem/11116

n = int(input())
for _ in range(n):
    sol = 0
    m = int(input())
    left = [*map(int, input().split())]
    right = [*map(int, input().split())]
    for i in range(0, m, 2):
        if left[i] < right[i]:
            sol += 1
    print(sol)
