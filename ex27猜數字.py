ans,dic=input(),{}
for i in ans: dic[i] = 1
while True:
    A,B,s=0,0,input()
    if int(s)==0: break
    for i in range(len(s)):
        A,B = A+(s[i]==ans[i]),B+(dic.get(s[i])!= None)
    print(f'{A}A{B-A}B')