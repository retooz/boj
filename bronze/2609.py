a, b = map(int, input().split())
m = a * b
a, b = min(a, b), max(a, b)
while a != 0 and b != 0:
    a, b = b % a, a
print(b)
print(m // b)