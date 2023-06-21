n=int(input())
print("NO" if (n%2==0 and n!=2) or sum([n%i==0 for i in range(3,int(n**0.5)+1,2)]) else "YES")