ISBN=list(map(lambda c:int(c) if c!='X' else 10,input().split()))
ISBN=[sum(ISBN[:i+1]) for i in range(len(ISBN))]
print("YES" if [sum(ISBN[:i+1]) for i in range(len(ISBN))][-1]%11==0 else "NO")