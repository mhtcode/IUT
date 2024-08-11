voroodi = input().split(' ')
kabise = []
for i in range(1399,-1,-4) :
    kabise.append(i)

def tdad_kabise(x) :
    tafazol = []
    n = 0
    if int(x[0]) < 1+int(x[1]) :
        for i in range(int(x[0]), 1+int(x[1])) :
            tafazol.append(i)

        for j in range(tafazol) :
            if tafazol[j] in kabise :
                n+=1
    else :
            for i in range(1+int(x[1]), int(x[0])) :
                tafazol.append(i)

            for j in range(tafazol) :
                if tafazol[j] in kabise :
                    n+=1

    return n


print(tdad_kabise(voroodi))