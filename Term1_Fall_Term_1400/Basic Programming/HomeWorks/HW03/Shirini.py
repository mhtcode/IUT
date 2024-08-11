r = int(input())
c = int(input())


r1 = r%10
r10 = r%100 - r1
r100 = r//100

R = 100*r1 + r10 + r100



c1 = c%10
c10 = c%100 - c1
c100 = c//100

C = 100*c1 + c10 + c100





if 999>= r >99 and 999>= c >99 :
     if   R<C :
          print(r ,'<', c)
     elif C<R :
          print(c ,'<', r) 
     else:
          print(r ,'=', c)     