a, b = map(int, input().split())
a, b = str(a)[::-1], str(b)[::-1]
if a > b:
    print(a)
else:
    print(b)