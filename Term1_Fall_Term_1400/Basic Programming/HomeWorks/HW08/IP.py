with open('input1.txt') as f1 :
    mohtava1 = f1.readlines()
with open('input2.txt') as f2 :
    mohtava2 = f2.readlines()
javab = []   

for i in mohtava1 :
    if i in mohtava2 :
        javab.append(i)
with open('output.txt','a') as out :
    for i in javab :
        out.write(i)
with open('output.txt') as output :       
    output = output.read()

print(output)