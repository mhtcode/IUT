m = int(input())
n = int(input())


def is_prime(n): 
    if n <= 1: 
        return False
    for i in range(2,n//2+1): 
        if n % i == 0: 
            return False
    return  True
  


str_javab = ''
space = ' '


javab = 0

if (m+n) % 2 == 1 :
    for p in range(m+1, n) :
        x = is_prime(p)
        while x :
            while p!=0 :
                javab+=p%10
                p//=10
                
            
            
            break
    print(javab)

else :
    x = 2
    y = 2
    for i in range(m+1, n) :
        if i%10 == 5 :
            i2 = i**2
            if i==5 :
                i = str(i)
                str_javab+=i+space
            elif i2%(10**x) == i :
                x+=1
                i = str(i)
                str_javab+=i+space
        elif i%10 == 6 :
            j2 = i**2
            if i==6 :
                i = str(i)
                str_javab+=i+space
            elif j2%(10**y) == i :
                y+=1
                i = str(i)
                str_javab+=i+space
    
    a = str_javab[0:-1]
    print(a)
    
    




            




        

