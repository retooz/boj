n = int(input())
q = sorted(list(map(int, input().split())))
m = q[-1]
ans = 0
for i in range(m, 1, -1):
    tmp = list(filter(lambda x: x >= i, q))
    if len(tmp) >= i:
        ans = i
        break
print(ans)