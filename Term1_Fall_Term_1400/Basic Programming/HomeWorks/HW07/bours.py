# ba arz poozesh code kamel nist ama talasham ghbel ehterame :)  

n = int(input())
maghsoum = []

def sumdigits (number) :

    sum=0

    while number != 0 :

        sum = sum + number % 10

        number = number / 10

    return sum



def avalboodan(x) :
    c=0
    for i in range(1,int(x)):
        if (int(x)%i==0):
            c+=1
    if (c==1):
        return True
    else:
        return False

def maghsoumel(number) :
    for i in range(1, number):
        if number % i == 0:
            maghsoum.append(number)
    return len(maghsoum)

def halghavi(m) :
    m = str(sabad[1])
    count = 0
    for i in range(len(m)) :
        if avalboodan(m) :
            count+=1
    if count==len(m) :
        sumdigits(m)


def soud()  :
    soud = 0
    zarb = 0
    jam = 0
    aval = []
    lst_soud = []
    
    for i in range(n) :
        sabad = input().split(' ')
        x = int(sabad[3])-int(sabad[4])

        if avalboodan(sabad[1]) :
            soud += halghavi(sabad[1])
        else :
            while x % prime == 0:
                x /= prime
                prime += 1
                aval.append(prime)
                soud+=(-len(aval))


        
        if abs(x) % maghsoumel(x) == 0 :
            x = str(x)
            for i in range(len(x)) :
                zarb *= int(x[i])
        else :
            x = int(x)
            prime = 2
            
            while x % prime == 0:
                x /= prime
                prime += 1
                aval.append(prime)
            for i in range(len(aval)) :
                jam += int(aval[i])

        if x>0 :
            soud+=jam+zarb
        else :
            soud+= (-jam)+(-zarb)

        if True:
            print(str(soud)+'%')
        lst_soud.append(soud)


soud()













