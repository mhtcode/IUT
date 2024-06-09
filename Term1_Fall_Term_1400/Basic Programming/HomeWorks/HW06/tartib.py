n = int(input())
   
def tartib() :
    k = 0
    lst1 = list(input())
    lst2 = list(input())
    for i in range(len(lst2)) :
        if lst2[i] in lst1 :
            a = 0
            if lst1.count(lst2[i]) > 1 :
                tekrar = i
                k = 1
        else :
            a = 1
            break
    def javab() :
        i = 0

        if  int(lst1.index(lst2[i])) < int(lst1.index(lst2[i+1])) :  
            while int(lst1.index(lst2[i])) < int(lst1.index(lst2[i+1])) :
            
                
                if i+1 == len(lst2)-1 :
                    print('YES')
                    break
                i+=1
            else :
                print('NO')
        else :
            while int(lst1.index(lst2[i])) > int(lst1.index(lst2[i+1])) :
            
                
                if i+1 == len(lst2)-1 :
                    print('YES')
                    break
                i+=1
            else :
                print('NO')    
        
    if a == 0  :
        javab()
    

    elif a != 0 :
        print('NO')

    
                
for i in range(n) :
    tartib()

# bug : agar harf tekrari dashte bashim