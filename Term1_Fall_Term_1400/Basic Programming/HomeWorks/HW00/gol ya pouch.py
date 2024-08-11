n = int(input())
first = input()
count = 0
for i in range(0, n+1) :
    livan1 = input()
    livan2 = input()
    if livan1 == first :
        first = livan2
    elif livan2 == first :
        first = livan1
    count+=1
    if count == n :
        break

print(first)













