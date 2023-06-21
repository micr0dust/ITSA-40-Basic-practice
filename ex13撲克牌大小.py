cases = int(input())
for i in range(cases):
    line = input().split()
    print(*sorted(line,key=lambda e:-(ord(e[0])*1000+len(e)*100+int(e[-1]))))