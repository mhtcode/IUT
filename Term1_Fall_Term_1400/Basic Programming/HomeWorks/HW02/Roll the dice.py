n = int(input())
x = int(input())
if n<2:
    print(x)
else:
    s = (x//6+1)*10**(n-1)

    t = x%6
    if t==0:
        t=6
        s=int((x/6)*10**(1))
    print(s+t)





