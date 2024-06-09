donbale = input().split(' ')
def hesabi(x) :
    d = ''
    
    d = int(x[1]) - int(x[0])
    for i in range(len(x)) :
        if int(x[i]) == (i*d) + int(x[0]) :
            a = 1
        else :
            a = 0
    if a == 1 :
        return True
    else :
        return False    


print(hesabi(donbale))

