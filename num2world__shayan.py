yektabist = [" ", "Yek", "Do", "Se", "Chahar", "Panj", "Shish", "Haft", "Hasht", "Noh", "Dah",
             "Yazdah", "Davazdah", "Sizdah", "Chahardah", "Panzdah", "Shanzdah", "Hefdah", "Hejdah", "Nuzdah"]
Dahgan = [" ", " ", "Bist", "Sih", "Chehel",
          "Panjah", "Shast", "Haftad", "Hashtad", "Navad"]
Sadgan = [" ", "Sad", "Dvist", "SiSad", "ChaharSad",
          "PanSad", "SheshSad", "HaftSad", "HashtSad", "NohSad"]
vahed = [" ", " ", " Hezar", " Million", " Milliard", " bilion", " Trillion", " Quadrillion", " Quintillion", " Sextillion", " Septillion",
         " 0Octillion", " Nonillion", " Decillion", " Undecillion", " Duodecillion", " Tredecillion", " Quattuordecillion",
         " Quindecillion", " Sexdecillion", " Septendecillion", " Octodecillion", " Novemdecillion"]
x =input("Enter The Number....")
# x1=int(x)*10
if int(x) == 0:
    print("sefr")
elif len(x) == 1:
    print(yektabist[int(x)])#+rial)))
elif len(x) == 2:
    dag = int(x)//10
    yek = int(x) % 10
    if dag == 1:
        print(yektabist[int(x)])#+rial)
    elif yek == 0:
        print(Dahgan[dag]+" " + yektabist[yek])#+rial)
    else:
        print(format(Dahgan[dag]+" " + "o"+" " + yektabist[yek]))#+"rial")
elif len(x) == 3:
    sad = int(x)//100
    dag = (int(x)//10) % 10
    yek = int(x) % 10
    s = (str(dag)+str(yek))
    if dag == 0 and yek == 0:
        print(Sadgan[sad]+Dahgan[dag]+yektabist[0])#+rial)
    elif dag == 0:
        print(Sadgan[sad]+" "+"o"+" "+yektabist[int(s)])#+"rial")
    elif dag == 1:
        print(Sadgan[sad]+" "+"o"+" "+yektabist[int(s)])#+rial)
    elif yek == 0:
        print(Sadgan[sad]+" "+"o"+" "+Dahgan[dag])#+rial)
    else:
        print(Sadgan[sad]+" "+"o"+" "+Dahgan[dag]+" "+"o"+" "+yektabist[yek])   #+rial)
else:
    n = len(x)
    d, r = divmod(n, 3)
    joda1 = []
    for i in range(d):
        joda1.append((x[n-(i*3)-3:n-(i*3)]))
    # print(joda1)
    joda2 = []
    joda2.append(x[0:r])
    # print(joda2)
    joda = joda1+joda2
    joda.reverse()
    # print(joda)
    javab = []
    for i in joda:
        if len(i) == 1:
            javab.append(yektabist[int(i)])
        elif len(i) == 2:
            dag = int(i)//10
            yek = int(i) % 10
            if dag == 1:
                javab.append(yektabist[int(i)])
            else:
                javab.append(Dahgan[dag]+" " + " " + yektabist[yek])
        elif len(i) == 3:
            sad = int(i)//100
            dag = (int(i)//10) % 10
            yek = int(i) % 10
            s = (str(dag)+str(yek))
            if sad == 0 and dag == 0 and yek == 0:
                javab.append("")
            elif sad == 0 and dag == 0:
                javab.append(yektabist[int(s)])
            elif sad == 0 and dag == 1:
                javab.append(yektabist[int(s)])
            elif dag == 1:
                javab.append(Sadgan[sad]+" "+"o"+" "+yektabist[int(s)])
            elif sad == 0:
                javab.append(Dahgan[dag]+"o" + yektabist[yek])
            elif dag == 0 and yek == 0:
                javab.append(Sadgan[sad])
            elif dag==0:
                javab.append(Sadgan[sad]+" "+"o"+" "+yektabist[yek])
            elif yek == 0:
                javab.append(Sadgan[sad]+" "+"o"+" "+Dahgan[dag])
            else:
                javab.append(Sadgan[sad]+" "+"o"+" " +
                             Dahgan[dag]+" "+"o"+" "+yektabist[yek])
    x = ''
    for i in range(len(javab)):
        if javab[i] == '':
            continue
        x += javab[i] + vahed[len(javab)-i]+" "+"o"+" "
    m = x.split()
    while m[len(m) - 1] == "o":
        m.pop(len(m) - 1)
    for i in m:
        # if i ==m[len(m)-1]:
        #     print(i+"rial", end=" ")
        # else:
        print(i, end=" ")
#code by Shayan Hashemi

