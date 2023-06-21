orders = int(input())
cars = list(map(int,input().split()))
schedule = [0]*(max(cars)+1)
for i in range(orders):
    for j in range(cars[2*i],cars[2*i+1]):
        schedule[j]+=1
print(max(schedule))