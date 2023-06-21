s=list(input())
print("YES" if s[:int(len(s)/2):1]==s[:int((len(s)-1)/2):-1] else "NO")