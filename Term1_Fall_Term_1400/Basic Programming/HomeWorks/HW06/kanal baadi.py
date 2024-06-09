a = input().split(' ')
lst_kanal = []
n = []

for i in range (int(a[0])) :
    kanal = input()
    lst_kanal.append(kanal)

    
start = int(a[1])-1
while int(a[-1]) + int(a[1]) > len(n) :
    n+=lst_kanal


print(n[start+int(a[-1])])