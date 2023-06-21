def complement(string):
    s=list(string)
    return ''.join(['0' if i=='1' else '1' for i in s])
def toBinary(n):
    res=''
    while n:
        res+=str(n%2)
        n=int(n/2)
    return ('0'*(8-len(res))+res[::-1])[1::]
n=int(input())
print('1'+complement(toBinary(n+1)) if n<0 else '0'+toBinary(n))