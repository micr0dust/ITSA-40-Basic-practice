idTable={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'J':18,'K':19,'L':20,'M':21,'N':22,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'X':30,'Y':31,'W':32,'Z':33,'I':34,'O':35}
idNum=input()
x1,x2,N=int(idTable[idNum[0]]/10),idTable[idNum[0]]-int(idTable[idNum[0]]/10)*10,[int(i) for i in idNum[1:]]
print("CORRECT!!!" if (x1+9*x2+8*N[0]+7*N[1]+6*N[2]+5*N[3]+4*N[4]+3*N[5]+2*N[6]+N[7]+N[8])%10==0 else "WRONG!!!")