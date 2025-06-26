isbn = input().strip()
n = 0
m = 0
check = int(isbn[12])
for i in range(12):
    if isbn[i] == "*":
        m = 1 if i % 2 == 0 else 3
    elif i % 2 == 0:
        n += int(isbn[i])
    else:
        n += int(isbn[i]) * 3

for i in range(10):
    total = n + i * m
    calculated = (10 - (total % 10)) % 10
    if calculated == check:
        print(i)
        break