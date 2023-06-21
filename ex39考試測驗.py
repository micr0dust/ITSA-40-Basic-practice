def check(lst):
    if min(lst)>=60 or (sum(lst)-min(lst)-max(lst)>=60 and sum(lst)>=220): return 'P'
    if (sum(lst)-min(lst)-max(lst)>=60 and sum(lst)<220) or (sum(lst)-min(lst)-max(lst)<60 and max(lst)>=80): return 'M'
    return 'F'
for i in range(int(input())):
    print(check(list(map(int,input().split()))))