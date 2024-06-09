x1 = int(input())
y1 = int(input())


x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

x4 = int(input())
y4 = int(input())

x5 = int(input())
y5 = int(input())



if x1==x2 or x1==x3 or x1==x4 or x1==x5 or x2==x3 or x2==x4 or x2==x5 or x3==x4 or x3==x5 or x4==x5  :
    print('Yes')


elif y1==y2 or y1==y3 or y1==y4 or y1==y5 or y2==y3 or y2==y4 or y2==y5 or y3==y4 or y3==y5 or y4==y5  :
    print('Yes')


elif ( (x2-x1)/(y2-y1)==1 or (x2-x1)/(y2-y1)==-1 or (x3-x1)/(y3-y1)==1 or (x3-x1)/(y3-y1)==-1 or (x4-x1)/(y4-y1)==1 or (x4-x1)/(y4-y1)==-1 or (x5-x1)/(y5-y1)==1 or (x5-x1)/(y5-y1)==-1) :  #movarab khooneh 1
    print('Yes')


elif ( (x3-x2)/(y3-y2)==1 or (x3-x2)/(y3-y2)==-1 or (x4-x2)/(y4-y2)==1 or (x4-x2)/(y4-y2)==-1 or (x5-x2)/(y5-y2)==1 or (x5-x2)/(y5-y2)==-1 ) :           #movarab khooneh 2
    print('Yes')


elif ( (x4-x3)/(y4-y3)==1 or (x4-x3)/(y4-y3)==-1 or (x5-x3)/(y5-y3)==1 or(x5-x3)/(y5-y3)==-1 or (x5-x3)/(y5-y3)==1 ) :             #movarab khooneh 3
    print('Yes')



elif ( (x5-x4)/(y5-y4)==1 or (x5-x4)/(y5-y4)==-1 ):              #movarab khooneh 4
    print('Yes')



else:
    print('No')        




 



