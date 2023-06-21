money,apple,orange,peach=map(int,input().split(','))
rest=money-apple*15-orange*20-peach*30
print("%d" % 0 if rest <0 else "%d,%d,%d" % (rest%5,int((rest%50)/5),int(rest/50)))