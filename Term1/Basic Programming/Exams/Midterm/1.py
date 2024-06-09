ebarat = input().split(' ')
def my_fun(x) :
    javab = []
    lst_len_ebarat = []
    for i in range(len(x)) :
        lst_len_ebarat.append(len(x[i]))
    for j in range(len(lst_len_ebarat)):
        javab.append(lst_len_ebarat.count(lst_len_ebarat[j]))
        javab.sort()
    max_tekrar = javab[-1]
    for k in range(len(lst_len_ebarat)) :
        if lst_len_ebarat.count(lst_len_ebarat[k]) == max_tekrar :
            return lst_len_ebarat[k]

        
    
        

  


print(my_fun(ebarat))

    