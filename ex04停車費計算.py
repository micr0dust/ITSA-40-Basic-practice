hrS,minS=map(int,input().split(' '))
hrE,minE=map(int,input().split(' '))
detla = (hrE-hrS)*60+minE-minS
def total(detla):
    cost = 0
    cost += int(detla/30)*30
    detla=detla-60*2
    if detla < 0: return cost
    cost += int(detla/30)*10
    detla=detla-60*2
    if detla < 0: return cost
    return cost + int(detla/30)*20
print(total(detla))