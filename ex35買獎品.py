for i in range(int(input())):
    T,m,k=map(int,input().split())
    t=sum(sorted(map(int,input().split()))[:m])
    print("Impossible" if T < t else t)