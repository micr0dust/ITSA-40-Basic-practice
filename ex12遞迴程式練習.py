def f(k):
    if k<=1:
        return k+1
    return f(k-1)+f(int(k/2))
print(f(int(input())))