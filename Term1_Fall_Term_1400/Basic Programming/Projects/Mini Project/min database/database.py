name = input()
with open(f'{name}.txt', 'a+') as data :
    data.write(name + '\n')
    

