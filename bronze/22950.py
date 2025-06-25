n = int(input())
bi = int(input().strip(), 2)
k = 2 ** int(input().strip())
if bi % k == 0:
    print("YES")
else:
    print("NO")