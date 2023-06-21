r,n,p,money=float(input()),int(input()),int(input()),0
for i in range(n):
    money=(money+p)+(money+p)*(r)
print(p if n==0 else int(money))