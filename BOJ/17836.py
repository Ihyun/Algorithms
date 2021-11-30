import copy
from collections import deque

N, M, T = map(int, input().split())
pan = []
for i in range(N):
    pan.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if pan[i][j] == 2:
            gramr = i
            gramc = j
            break

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque()

chk = copy.deepcopy(pan)
queue.append([0, 0, 0])
chk[0][0] = 1
sol = -1

while queue:
    outq = queue.popleft()
    if outq[0] == N-1 and outq[1] == M-1:
        sol = outq[2]
        break
    for i in range(4):
        nr = outq[0]+dr[i]
        nc = outq[1]+dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if chk[nr][nc] != 1:
                queue.append([nr, nc, outq[2]+1])
                chk[nr][nc] = 1

queue.clear()
chk = copy.deepcopy(pan)
queue.append([gramr, gramc, 0])
chk[gramr][gramc] = 1
gramsol = -1

while queue:
    outq = queue.popleft()
    if outq[0]==0 and outq[1]==0:
        gramsol = outq[2]
        break
    for i in range(4):
        nr = outq[0]+dr[i]
        nc = outq[1]+dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if chk[nr][nc] != 1:
                queue.append([nr, nc, outq[2]+1])
                chk[nr][nc] = 1

if gramsol != -1:
    gramsol += (N-1-gramr) + (M-1-gramc)
    if sol == -1:
        if gramsol <= T:
            print(gramsol)
        else:
            print("Fail")
    else:
        if min(gramsol, sol)<=T:
            print(min(gramsol, sol))
        else:
            print("Fail")
else:
    if sol == -1:
        print("Fail")
    elif sol <= T:
        print(sol)
