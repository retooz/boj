t = int(input())

for _ in range(t):
    input()
    j, b = map(int, input().split())
    jb = sorted([i for i in map(int, input().split())])
    bb = sorted([i for i in map(int, input().split())])

    while jb and bb:
        if jb[0] < bb[0]:
            jb.pop(0)
        elif jb[0] > bb[0]:
            bb.pop(0)
        else:
            bb.pop(0)
            
    if jb:
        print("S")
    elif bb:
        print("B")
    else:
        print("C")