while True:
    try:
        dic={}
        for i in input().split():
            dic[i]=1 if dic.get(i)==None else dic[i]+1
        print([key for key, value in dic.items() if value == max(dic.values())][0] if max(dic.values())>int(sum(dic.values())/2) else "NO")
    except:break