lst = input().split(' ')
gheymat_prime = input().split(' ')

n = int(lst[0])
k = int(lst[1])
gheymat_prime.sort()








def cake() :
    javab = []
    lst_entekhab = []
    for i in range(k) :
        lst_entekhab.append([])
    
    if k>1 :
        j = 0
        lst_entekhab[j].append(gheymat_prime[j])
        j = 1
        i = 1
        count = 1
        while j <k :
            if count == len(gheymat_prime) :
                break
            if not gheymat_prime[i]  in lst_entekhab[j] :
                lst_entekhab[j].append(gheymat_prime[i])
                j+=1
                i+=1
                count+=1
                if j==k :
                    j=1
            else :
                lst_entekhab[0].append(gheymat_prime[i])
                count+=1
        for i in range(k) :
            javab.append(max(lst_entekhab[i]))
        javab.sort()
        return javab[0]
    else :
        lst_entekhab = gheymat_prime            
        return lst_entekhab[-1]     
           
        
                
            
print(cake())











    


