# https://www.acmicpc.net/problem/1535

global N, hps, dls, sol
N = int(input())
hps = list(map(int, input().split()))
dls = list(map(int, input().split()))
sol = 0


def chk(i, hp, dl):
    global sol

    if hp <= 0:
        return

    if i == N:
        if sol < dl:
            sol = dl
        return

    chk(i+1, hp-hps[i], dl+dls[i])
    chk(i+1, hp, dl)
    return


chk(0, 100, 0)
print(sol)
