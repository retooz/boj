a = 0
count = [0] * 1001
for _ in range (10):
    inp = int(input())
    a += inp
    count[inp] += 1
print(a // 10)
print(count.index(max(count)))