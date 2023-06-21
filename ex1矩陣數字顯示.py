dic={'1':[0, 0, 1, 0, 0, 1, 0],'2':[1, 0, 1, 1, 1, 0, 1],'3':[1, 0, 1, 1, 0, 1, 1],'4':[0, 1, 1, 1, 0, 1, 0],'5':[1, 1, 0, 1, 0, 1, 1],'6':[1, 1, 0, 1, 1, 1, 1],'7':[1, 0, 1, 0, 0, 1, 0],'8':[1, 1, 1, 1, 1, 1, 1],'9':[1, 1, 1, 1, 0, 1, 0],'0':[1, 1, 1, 0, 1, 1, 1]}
def row(front, mid, end): return ('*' if front else ' ')+('***' if mid else '   ')+('*' if end else ' ')
ipt = [dic[i] for i in list(input())]
print(*[row(i[0] or i[1], i[0], i[0] or i[2]) for i in ipt])
print(*[row(i[1], 0, i[2]) for i in ipt])
print(*[row(i[1] or i[3] or i[4], i[3], i[2] or i[3] or i[5]) for i in ipt])
print(*[row(i[4], 0, i[5]) for i in ipt])
print(*[row(i[4] or i[6], i[6], i[5] or i[6]) for i in ipt])