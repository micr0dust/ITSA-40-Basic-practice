sentence = input().split()
print(len(sentence))
dic = {}
line = ''.join(sentence).lower()
for i in line:
    if i.isalpha():
        dic[i]= 1 if dic.get(i)==None else dic[i]+1
for i in sorted([key for key in dic]):
    print(i+' : '+str(dic[i]))