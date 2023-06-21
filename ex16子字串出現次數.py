sub,main=input(),input()
count = 0
for i in range(len(main)-len(sub)+1):
    if sub[::]==main[i:len(sub)+i:]:
        count+=1
print(count)