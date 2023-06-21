lst,dic=[int(input()) for i in range(4)],{}
for i in lst: dic[i]= 1 if dic.get(i)==None else dic[i]+1
if len(dic.keys()) == 1 : print("WIN")
elif len(dic.keys())<=3 and max(dic.values())<3: print(sum([key*value for key,value in dic.items()])-min([key for key,value in dic.items() if value>=2])*2)
else: print("R")