for i in range(int(input())): print(*sorted(input().split(),key=lambda n:-(ord(n[0])*100+int(n[1:3]))))