while True :
    data = sorted([i for i in map(int, input().split())])
    if len(set(data)) == 1 and list(set(data))[0] == 0:
        break    
    if data[0]**2 + data[1]**2 == data[2]**2:
        print("right")
    else:
        print("wrong")