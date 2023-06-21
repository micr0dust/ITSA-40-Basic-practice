def isBissextile(y):
    if y%400==0: return "Bissextile Year"
    if y%100==0: return "Common Year"
    if y%4==0: return "Bissextile Year"
    return "Common Year"
while True:
    try:
        print(isBissextile(int(input())))
    except:break