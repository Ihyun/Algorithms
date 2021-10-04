# https://www.acmicpc.net/problem/11899

s = input()
val = 0
minval = 0

for c in s:
    if c == '(':
        val += 1
    elif c == ')':
        val -= 1
        if minval > val:
            minval = val

print(minval * -2 + val)
