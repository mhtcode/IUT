a = int(input())
def varoon(x) :
    
    x = str(x)
    y = x[::-1]
    for i in range(len(y)) :
        while int(y[i]) == 0 :
            y = list(y)
            y.remove(y[i])
        y = ''.join(y)
        break

    x = int(x)
    y = int(y)
    if x < y :
        return y-x
    else :
        return x-y






print(varoon(a))