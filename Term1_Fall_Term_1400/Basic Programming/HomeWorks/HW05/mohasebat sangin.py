v = input().split(' ')    # voroodi
a = int(v[0])
x = int(v[1])
n = int(v[2])

d = 0

for k in range(0, n+1) :
    nf = 1            # n factorial
    for i in range (1, n+1) :
        nf = nf*i
    
    

    kf = 1            # k factorial
    for i in range (1, k+1) :
        kf = kf*i
    
    


    r = n-k
    rf = 1            # n-k factorial
    for i in range (1, r+1) :
        rf = rf*i
    
    
   

    entekhab = nf / (rf * kf)



    s = int(entekhab * (x**k) * (a**r))        
    

    d = s + d      # javab nahaie
    
    k+=1

print(d)



    


   