lst = input().split(' ')
lst_goals = input().split(' ')
nime_avval = []
nime_dovvom = []
for j in range (len(lst_goals)) :
    j = 0
    if lst_goals == [] :
        break
    if -1 < int(lst_goals[j]) < 46+int(lst[1]) :
        nime_avval.append(lst_goals[j])
        lst_goals.remove(lst_goals[j])
    else :
        break    


for i in range (len(lst_goals)) :
    i = 0
    if lst_goals == [] :
        break
    if 45 < int(lst_goals[i]) < 91+int(lst[2])  :
        nime_dovvom.append(lst_goals[i])
        lst_goals.remove(lst_goals[i])





if len(nime_dovvom)+len(nime_avval) == int(lst[0]) :
    print('YES')
else :
    print('NO')