while True:
    try:
        row,col=map(int,input().split())
        vector=[[0]*row for i in range(col)]
        for i in range(row):
            line=list(input().split())
            for j in range(col):
                vector[j][i]=line[j]
        for item in vector:
            print(*[j for j in item])
    except: break