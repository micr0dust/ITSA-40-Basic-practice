n,summer,nonsummer=int(input()),0,0
table=[[0,120,330,500,700,float("inf")],[0,2.10,3.02,4.39,4.97,5.63],[0,2.10,2.68,3.61,4.01,4.50]]
def total(n,summer,nonsummer):
    for i in range(5):
        summer,nonsummer=summer+n*(table[1][i+1]-table[1][i]),nonsummer+n*(table[2][i+1]-table[2][i])
        n-=table[0][i+1]-table[0][i]
        if n<0: return (summer,nonsummer)
    return (summer,nonsummer)
print("Summer months:%.2f\nNon-Summer months:%.2f"%total(n,0,0))