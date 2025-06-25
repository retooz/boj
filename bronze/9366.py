for _ in range(1, int(input()) + 1):
    a, b, c = sorted(list(map(int, input().split())))
    if a + b <= c:
        print(f"Case #{_:d}: invalid!")
    elif a == b == c:
        print(f"Case #{_:d}: equilateral")
    elif a == b or b == c or c == a:
        print(f"Case #{_:d}: isosceles")
    else:
        print(f"Case #{_:d}: scalene")