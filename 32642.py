n = int(input())
b = [0] * n
w = [i for i in map(int, input().split())]
for i in range(n):
    if i == 0:
        b[i] = 1 if w[i] == 1 else -1
    else:
        b[i] = b[i - 1] - 1 if w[i] == 0 else b[i - 1] + 1
print(sum(b))