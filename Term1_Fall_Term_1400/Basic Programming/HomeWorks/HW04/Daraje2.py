a = float(input())
b = float(input())
c = float(input())

if (-100<=a<=100) and   (-100<=b<=100)  and (-100<=c<=100) :
    
    d = int((b**2)-(4*a*c))     # delta
    
    d1 = (d)**(1/2)
    
    
    if a==0 and b!=0 :
        x = -c/b
        print("{:.3f}".format(x))
    
    
    elif d<0 or (a==0 and b==0) :
        print('IMPOSSIBLE')

    

    elif a!=0:
        x = (-b + d1) / (2*a)              # RISHE 1
    
    
        
        y = (-b - d1) / (2*a)             # RISHE 2
        
        
        if x < y :
            print("{:.3f}".format(x))
            print("{:.3f}".format(y))
        elif x > y :
            print("{:.3f}".format(y))
            print("{:.3f}".format(x))
        else:
            print("{:.3f}".format(x))
        

  
    











