# Q: https://www.acmicpc.net/problem/11899

s = input()
val = 0
vals = [0]

for c in s:
    if c == '(':
        val += 1
        vals.append(val)
    elif c == ')':
        val -= 1
        vals.append(val)

ans = min(vals) * -1
ans += vals[-1] + ans
print(ans)
