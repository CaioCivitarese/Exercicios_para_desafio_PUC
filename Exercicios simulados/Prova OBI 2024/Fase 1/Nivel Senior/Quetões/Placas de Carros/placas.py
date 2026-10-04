P = input()
Plist = list(P)
ListaPlaca = []
StringPlaca = 0


if len(Plist) == 8:
    for caractere in Plist:
        
        if caractere.isalpha() == True:
            ListaPlaca.append("L")
        elif caractere.isdigit() == True:
            ListaPlaca.append("I")
        elif caractere == "-":
            ListaPlaca.append("-")

    StringPlaca = "".join(ListaPlaca)

    if StringPlaca == "LLL-IIII":
        print(1)
    else:
        print(0)

elif len(Plist) == 7:
    for caractere in Plist:

        if caractere.isalpha() == True:
            ListaPlaca.append("L")
        elif caractere.isdigit() == True:
            ListaPlaca.append("I")
        elif caractere == "-":
            ListaPlaca.append("-")

        StringPlaca = "".join(ListaPlaca)

    if StringPlaca == "LLLILII":
        print(2)
    else:
        print(0)

else:
    print(0)