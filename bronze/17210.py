s = int(input())
f = True if int(input()) == 1 else False
for _ in range(s-1):
    if s > 5 :
        print("Love is open door")
        break
    f = not f
    print(1 if f else 0)