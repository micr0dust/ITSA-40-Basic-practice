s,n=list(input()),int(input())
for i in range(len(s)):
    if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
        s[i]=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
    elif ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
        s[i]=chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    elif ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
        s[i]=chr((ord(s[i])-ord('0')+n)%10+ord('0'))
print(''.join(s))