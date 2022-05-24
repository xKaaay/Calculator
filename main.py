version = "/ Version = 0.2"
# to clear the console
import os
import re
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# This will be for later
length = False
tries = 0
exitc = 0
tm = 0
sep = "-" * 80
language = 0
title = "<|>  xKaaay Calculator " + version + "  <|>"
print(title.center(80, " "))

# List of the variations depending on the language / [0] = Spanish, [1] = English)
l = [["\n[!] Demasiados intentos fallidos [!]\n", "=> Opción: ", "\n                     [!] Por favor, elije según el menú. [!]\n", "\n[!] Has intentado demasiadas veces valores erroneos. [!]\n", \
"=> Por favor, digita tu suma con [+] : ", "[!] = Sólo hay un valor para sumar, agrega más. o no estás usando el signo correcto", "\n[!] El resultado de la suma es: ", \
"\n=> Quieres hacer otra suma o ir al menú? [SUMA - MENU - SALIR] : ", "\n[!] = Gracias por usar la calculadora.   /  xKaaay. [!]\n", \
"=> Por favor, digita tu resta con [-] : ", "\n[!] El resultado de la resta es: ", "\n=> Quieres hacer otra resta o ir al menú? [RESTA - MENU - SALIR] : "], \
    ["\n[!] Too many wrong attemps [!]\n", "=> Option: ", "\n                     [!] Please, select according to the menu. [!]\n", "\n[!] You've tried wrong values too many times. [!]\n", \
"=> Please, type your addition with [+] : ", "[!] = There's only one digit, add more. or you're not using the right sign", "\n[!] The total of the addition is: ", \
"\n=> Want to do another addition or go to menu? [ADDITION - MENU - EXIT] : ", "\n[!] = Thanks for using the calculator.   /  xKaaay. [!]\n", \
"=> Please, type your subtract with [-] : ", "\n[!] The total of the subtract is: ", "\n=> Want to do another subtract or go to menu? [SUBTRACT - MENU - EXIT] : "]]

# There are some people that just want the world burn
def Curious(listvar):
    listvar = re.sub("[,;.:_<>{^}´¨~¿¡'?)(&%$#!|°¬a'bcdefghijklmnopqrstuvwxyzñ ]","",listvar)
    return listvar

# Converting evetyrhing into a list to do the math
def split(vsplit):
    global indexSubs
    if "*" in vsplit:
        vsplit = re.sub("[-+/]", "", vsplit)
        vsplit = vsplit.split("*")
    
    if "/" in vsplit:
        vsplit = re.sub("[-+*]", "", vsplit)
        vsplit = vsplit.split("/")

    if "+" in vsplit:
        vsplit = re.sub("[-/*]", "", vsplit)
        vsplit = vsplit.split("+")
    
    if "-" in vsplit:
        vsplit = re.sub("[*+/]", "", vsplit)
        if vsplit.startswith("-") or "-" in vsplit[0]:
            indexSubs = True
        else: 
            indexSubs = False
        vsplit = vsplit.split("-")

    if type(vsplit) is not type(l):
        return [vsplit]
    else:
        return vsplit

# Addition formula
def addition():
    global length
    global tries
    global exitc

    while length == False:
        tries += 1
        if tries > 3:
            print(l[lS][3]) # [3] = You've tried wrong values too many times.
            break

        var = input(l[lS][4]) # [9] = Please, type your addition with [+].
        var = Curious(var)
        var = split(var)

        if len(var) <= 1:
            print(l[lS][5] + "[+]. [!]") # [5] = There's only one digit, add more. or you're not using the right sign [+].
            print(sep)
        else:
            if "" in var:
                for i in range(var.count("")):
                    var.remove("")
            res = 0
            for i in range(len(var)):
                op = int(var[i])
                res += op
            length = True
            print(sep)
            print(l[lS][6], res, " [!]\n") # [6] = The total of the addition is.
            print(sep)
            exitm = input(l[lS][7]) # [7] = Want to do another addition or go to menu? [ADDITION - MENU - EXIT].
            exitm = exitm.lower()
            if exitm == "suma" or "suma" in exitm or exitm == "addition" or "addition" in exitm:
                print("\n", sep)
                tries, length = 0, False

            elif exitm == "menu" or "menu" in exitm:
                clear()
                tries, length, exitc = 0, False, 0
                break
            else:
                print("\n", sep)
                print(l[lS][8]) # [8] = Thanks for using the calculator.
                print(sep)
                break

def subtract():
    global length
    global tries
    global exitc

    while length == False:
        tries += 1
        if tries > 3:
            print(l[lS][3]) # [3] = You've tried wrong values too many times.
            break

        var = input(l[lS][9]) # [4] = Please, type your subtract with [-].
        var = Curious(var)
        var = split(var)        


        if len(var) <= 1:
            print(l[lS][5], "[-]. [!]") # [5] = There's only one digit, add more. or you're not using the right sign.
            print(sep)
        else:
            if "" in var:
                for i in range(var.count("")):
                    var.remove("")
            res = 0
            for i in range(len(var)):
                if indexSubs:
                    op = int(var[i])
                    res -= op
                else:
                    op = int(var[i])
                    res = int(var[0])
                    res -= op
            length = True
            print(sep)
            print(l[lS][10], res, " [!]\n") # [6] = The total of the subtract is.
            print(sep)
            exitm = input(l[lS][11]) # [11] = Want to do another subtract or go to menu? [SUBTRACT - MENU - EXIT].
            exitm = exitm.lower()
            if exitm == "resta" or "resta" in exitm or exitm == "subtract" or "subtract" in exitm:
                print("\n", sep)
                tries, length = 0, False

            elif exitm == "menu" or "menu" in exitm:
                clear()
                tries, length, exitc = 0, False, 0
                break
            else:
                print("\n", sep)
                print(l[lS][8]) # [8] = Thanks for using the calculator.
                print(sep)
                break


# Second menu with all the options available
def menu():
    global length
    global tries
    global exitc
    global tm

    while exitc == 0:
        tm += 1
        exitc = 1
        print(sep)
        if lS == 0:  #If the user has chosen spanish
            print(""" 
            Elegiste español, estas son las opciones:

            [1] = Suma.
            [2] = Resta.
            [3] = Multiplicación. [Aún no]
            [4] = División. [Aún no]
            [5] = Salir. [Aún no]
            """)
        else: #If the user has chosen english
            print(""" 
            You've chosen english, these are the options:

            [1] = Addition.
            [2] = Subtraction.
            [3] = Multiplication. [Not yet]
            [4] = Division. [Not yet]
            [5] = Exit. [Not yet]
            """)
        if tm > 3:
            clear()
            print(sep)
            print(l[lS][0]) # [0] = Too many wrong attemps. 
            print(sep)
            break
        else:
            print(sep)
            opc = input(l[lS][1]) # [1] = Option:
            opc = opc.lower()

            if opc == "suma" or opc == "1" or "suma" in opc or opc == "addition" or "addition" in opc:
                clear()
                addition()
            elif opc == "resta" or opc == "2" or "resta" in opc or opc == "subtraction" or "subtraction" in opc:
                clear()
                subtract()
            else:
                clear()
                print(sep)
                print(l[lS][2]) # [2] = Please, select according to the menu.
                exitc = 0

# First menu, select the language
while language == 0:
    language = 1
    print(sep)
    print("Select a language | Elije un idioma")
    print("""
    [1] = Español
    [2] = English
    """)
    print(sep)
    langSel = input("=> ")
    langSel = langSel.lower()
    if langSel == "1" or langSel == "español" or "español" in langSel:
        lS = 0
        clear(), menu()
    elif langSel == "2" or langSel == "english" or "enlish" in langSel:
        lS = 1
        clear(), menu()
    else:
        clear()
        print(sep)
        print("\n   [!] Wrong command / Comando erroneo[!]\n")
        language = 0
