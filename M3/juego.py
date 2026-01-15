###Librerias###

import modulo_dic_fun as mod

juan = mod.getIdGames()

print(juan)


a = [iter([1,2,3]),iter([1,2,3,4,5,6])]

check = [True,True]

while any(check):
    for i in a:
        for j in i:
            try:
                next(i)
                print(j)
                break
            except:
                check[i] = False

print("finish")
