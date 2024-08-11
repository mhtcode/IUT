a = int(input())
b = int(input())
c = int(input())
d = int(input())

# 1 => IUT operator:
def dolar(x,y) :
    
    m1 = ''
    
    while True :
        for i in range(10) :
            while y!=0 :
                yekan_y = y%10
                y//=10
                yekan_y = str(yekan_y)
                break
            while x!=0 :
                yekan_x = x%10
                yekan_x = str(yekan_x)
                x//=10
                break
            if x==0 and y==0 :
                m1 = yekan_x + yekan_y + m1
                break
            m1 = yekan_x + yekan_y + m1
            
        return int(m1)

# base 10 to base c :
def base(base10, base_c) :
    javab = ''
    baghimande = base10%base_c
    while base10!=0 :
        
        base10//=base_c
        baghimande = str(base10%base_c) + str(baghimande)
        
        if base10 == 0 :
            javab = str(base10) + str(baghimande) + javab
    return int(javab)


# 3 => IUT number:
def palindrome(x) :
    m1 = ''
    x1 = str(x)
    while x!=0 :
        yekan_x = x%10
        yekan_x = str(yekan_x)
        x//=10
        
        m1 += yekan_x
    if x1 == m1 :
        print(True)
    else :
        print(False)
        
m = str(base(dolar(a,b), c))
x = int(m, d)
print(x)
palindrome(x)