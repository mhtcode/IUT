k = int(input())

j = str(1)
count = 0

for i in range (2, 5001) :
    a = str(i)
    j = j + a
    lst = list(j)
    
    if count+1==k :
        print(lst[k-1])
        break

    count+=1

