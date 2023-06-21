while True:
    try:
        lst=list(map(int,input().split()))
        print('Size: %d\nAverage: %.3f'% (len(lst),sum(lst)/len(lst)))
    except:break