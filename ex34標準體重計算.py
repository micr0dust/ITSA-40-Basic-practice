while True:
    try:
        height,gender=map(int,input().split())
        print("%.1f"% ((height-70)*0.6 if gender-1 else (height-80)*0.7))
    except:break