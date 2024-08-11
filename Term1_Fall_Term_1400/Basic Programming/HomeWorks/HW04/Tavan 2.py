n = int(input())
a = 0
while n> 0 :
    
    b = 2**a


    a+=1
    if b>n :
        print(2**(a-1))
        break

