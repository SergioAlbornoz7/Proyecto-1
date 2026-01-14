###Librerias###

import modulo_dic_fun as mod

a = iter(["juan","rodolfo","antono"])
b = iter(["chino","español","antonio","paco","meritchell"])
a2 = ""
b2 = ""
while a or b:
    for i in a:
        print("a")
        if len(a2)+ len(i) > 10:
            print(a2)
            a2 = ""
            break
        else:
            a2 += i
    for i in b:
        print("b")
        if len(b2)+ len(i) > 10:
            print(b2)
            b2 = ""
            break
        else:
            b2 += i