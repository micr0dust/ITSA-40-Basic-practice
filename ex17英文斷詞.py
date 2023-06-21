s=input().split()
print(*list(dict.fromkeys([i.lower() for i in s])))