n = int(input())
lst = input().split(' ')
a = 0
b = 0
x = 0


for i in range(n-1) :     
    if lst[x]>=lst[x+1]  :
        if a == n-1 :
            break
        while lst[x]>=lst[x+1]  :        #no zoul
                
            a+=1
            
            if x == n-2 :
                break
            x+=1

    elif  lst[x]<=lst[x+1]  :            #so oud
        if b == n-1 :
            break
        while lst[x]<=lst[x+1] :
            
            b+=1
            if x == n-2 :
                break
            x+=1




if a+b==n-1 :
    print('Yes')
elif a+b==2*(n-2) :
    print('Yes')
else :
    print('No')

     

        
  
        
        
        
        
    
            
 
     

        


        

