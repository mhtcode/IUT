n = int(input())
h = '#'
space = ' '
i = 4
j = n-1



for satr in range(1,(n+1)//2+1) :
    if satr==1 :
        print(n*h)
        continue
    while satr<(n+1)//2 :
        print(h+(satr-2)*space+h+(n-i)*space+satr*h)
        
        if n-i == 0 :
            break
        i+=2
        satr+=1
    break
if n!=1 :
    print(h+(satr-2)*space+satr*h)
satr+=1

while (n+1)//2 < satr < n+1 :
    while satr<n :
        if satr==n//2+2 :
            satr2 = satr-2
            left = n-3-satr2
        print(h+(left)*space+h+(n-j)*space+satr2*h)
        if left==0 :
            break
        satr+=1
        j-=2
        satr2-=1
        left-=1
    if 3<n<5 :
        if satr==n-1 :
            print(n*h)
            break
    elif n==3 :
        print(n*h)
        break
    else :
        print(n*h)
        break
    
    
        




        
    

        


    

    
    
        


    
