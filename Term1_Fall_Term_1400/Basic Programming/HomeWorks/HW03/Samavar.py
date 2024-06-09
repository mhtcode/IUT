T = int(input())
if 6000>=T>-273:
    if 6000>=T>100:
        print('Steam')
    elif -273<T<0:
        print('Ice')
    else:
        print('Water') 