n = int(input())

def Pascal(n) : 
      
    
    for line in range(n) : 
          
        for i in range(line + 1) : 
            print(zarib2jomleie(line, i), " ", end = "") 
        print('') 
      
  

def zarib2jomleie(n, k) : 
    natije = 1
    
    for i in range(0 , k) : 
        natije *= (n - i) 
        natije //= (i + 1) 
      
    return natije 
  


Pascal(n) 
  
  
