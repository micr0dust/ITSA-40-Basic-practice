cases = int(input())
for i in range(cases):
    op,a1,b1,a2,b2=input().split(' ')
    a1,b1,a2,b2=map(int,[a1,b1,a2,b2])
    print(*([a1-a2,b1-b2] if op=='-' else [a1+a2,b1+b2] if op=='+' else [a1*a2-b1*b2,a1*b2+b1*a2]))
    # if op=='-':
    #     print(*[a1-a2,b1-b2])
    # elif op=='+':
    #     print(*[a1+a2,b1+b2])
    # elif op=='*':
    #     print(*[a1*a2-b1*b2,a1*b2+b1*a2])