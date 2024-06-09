lst = input().split(' ')
a = int(lst[0])
b = int(lst[2])

SH = 0
N = 0
M = 0
A = 0

for i in range(0, 10**2) :
    if i%4 == 0 :
        a-=1
        SH+=1
    elif i%4 == 1 :
        b-=1
        N+=1
    elif i%4 == 2 :
        a-=1
        M+=1
    else :
        b-=1
        A+=1
    
   
    if a == 0 or b == 0 :
        print(SH,N,M,A)
        break


