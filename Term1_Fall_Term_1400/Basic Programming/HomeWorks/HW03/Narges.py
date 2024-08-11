n = int(input())
if 2<=n<=100000 :
  a = n//2
  a1 = ' 2'
  b = n%2


  if b==1:
      c = f'3{(a-1)*a1}'
      print(a)
      print(c)


  if b == 0:
      d = f'2{(a-1)*a1}'
      print(a)
      print(d)    
   


