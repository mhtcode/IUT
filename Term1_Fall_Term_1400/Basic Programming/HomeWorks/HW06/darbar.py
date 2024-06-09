lst = input().split(' ')

def bohloolo(lst) :
    
    
    if '#' in lst[0] :
        for i in range(1,len(lst[0])) :
            A = str( int(lst[-1])-int(lst[2])+1 )
            m = lst[0]
            if A[-i] == m[-i] :
                continue
            elif '#' != m[-i] :
                print(-1)
                return -1
            else :
                continue


        lst[0] = str( int(lst[-1])-int(lst[2]) )
        print(lst[0] + ' ' + '+' + ' ' + lst[2] + ' ' + '=' + ' ' + lst[-1] )

    elif '#' in lst[2] :
        for i in range(1,len(lst[2])+1) :
            A = str( int(lst[-1])-int(lst[0]) )
            m = lst[2]
            if A[-i] == m[-i] :
                
                continue
            elif '#' != m[-i] :
                print(-1)
                return -1
            else :
                continue
            


        lst[2] = str( int(lst[-1])-int(lst[0]) )
        print(lst[0] + ' ' + '+' + ' ' + lst[2] + ' ' + '=' + ' ' + lst[-1] )


    else :
        lst[-1] = str( int(lst[0])+int(lst[2]) )
        print(lst[0] + ' ' + '+' + ' ' + lst[2] + ' ' + '=' + ' ' + lst[-1] )

   
                    
                
                
           





bohloolo(lst)