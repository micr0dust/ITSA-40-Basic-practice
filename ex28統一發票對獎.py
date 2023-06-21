sp,head,cases,win,price=input(),[input(),input(),input()],int(input()),[0]*7,0  
table=[[item[j::] for j in range(6)] for item in head]  
def priceTable(n):   
    win[n]+=1   
    if n==0: return 2000000   
    if n==1: return 200000   
    if n==2: return 40000   
    if n==3: return 10000   
    if n==4: return 4000   
    if n==5: return 1000   
    if n==6: return 200   
def isWin(s):   
    if s==sp:   
        return priceTable(0)   
    for j in range(6):   
        nows=s[j:]  
        if table[0][j]==nows or table[1][j]==nows or table[2][j]==nows:  
            return priceTable(j+1)  
    return 0  
for i in range(cases):   
    price+=isWin(input())   
print(*win)   
print(price)