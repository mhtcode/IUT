N = int(input())
a = N-1
z = 0
while 2<N<20001 :
    
    if a==0 :
        break
    
    
    b = N%a
    a-=1
    
    
    if b==0 :
        d = a+1
        z = z+d



        
if z==N :
    print('YES')
     
if z!=N :
    print('NO')
    

            
             
        

