# https://www.acmicpc.net/problem/5957

import sys

N = int(input())
dishes = [list((range(N, 0, -1))), [], []]

for line in sys.stdin:
    try:
        ci, di = map(int, line.split())
    except:
        break
    for i in range(di):
        dishes[ci].append(dishes[ci - 1].pop())

for i in range(len(dishes[2]) - 1, -1, -1):
    print(dishes[2][i])
