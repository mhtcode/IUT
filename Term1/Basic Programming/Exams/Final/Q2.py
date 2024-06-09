tedad = int(input())
lst1 = input().split('=')
lst_chap_adad = []
zarib_x = []

chap = lst1[0].split('+')
rast = lst1[1].split('+')
for i in range(len(chap)):
    L_lst = list(chap[i])
    if 'x' in L_lst:
        L_lst.remove('x')
        for i in L_lst:
            zarib_x.append(i)
    else:
        for i in L_lst:
            lst_chap_adad.append(i)

for i in range(len(rast)):
    L_lst = list(rast[i])
    if 'x' in L_lst:
        L_lst.remove('x')
        for i in L_lst:
            zarib_x.append(i)
    else:
        for i in L_lst:
            lst_chap_adad.append(i)
