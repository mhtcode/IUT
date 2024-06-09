n = int(input())
d = 1          #ghadr nesbat
a = 1

if 1<n<101 :
    while n!=1 :
        if n%2 == 0 :
            n/=2
            d*=2
            a

        else:
            n//=2
            d*=2
            a+=d

    print(a)
