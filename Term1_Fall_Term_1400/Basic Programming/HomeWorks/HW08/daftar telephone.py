
# rahnama : 
#     n = 1 => ezafe kardan contact
#     n = 2 => moshahede etelaat contacts
#     n = 3 => list tamam contact ha
#     n = 4 => hazf hame
#     n = 5 => bastan file
 
while 1 :
    try :
        n = int(input())
        with open('database.txt','a') as f :

            with open('database.txt','r') as f1 :
                javab = f1.readlines()
            
            if n == 1 :
                contact = input()
                number = input()
                c = contact+'\n'
                n = number
                if c in javab :
                    j = javab.index(c)
                    javab[j+1] = n
                    with open('database.txt','w') as f2 :
                        f2.writelines(javab)
                else:
                    f.write('\n'+ c)
                    f.write(n)
                print('Contact was saved')

            elif n == 2 :
                contact = input()
                b = contact+'\n'
                if  b in javab :
                    i = javab.index(b)
                    number = javab[i+1][:-1]
                    print(number)
                else :
                    print('Unknown Contact')

            elif n == 3 :
                
                if len(javab) == 0 :
                    print('No contact found')
                else :
                    with open('database.txt','r') as f1 :
                        lst_contact = f1.read()
                        print(lst_contact)

            elif n == 4 :
                f = open('database.txt','w')
                print('All contacts were deleted')
                f.close()

            else :
                break
    except :
        print('Unable to open the file')
        
