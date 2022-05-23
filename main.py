# to clear the console
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# This will be for later
length = False
tries = 0
exitc = 0
tm = 0
sep = "-" * 80
language = 0
title = "|Calculadora v0.1 - xKaaay|"
print(title.center(80, "="))

# List of the variations depending on the language (0 = Spanish, 1 = English)
l = [["\n[!] Demasiados intentos fallidos [!]\n", "=> Opción: ", "\n                     [!] Por favor, elije según el menú. [!]\n", "                             [!] Has intentado demasiadas veces valores erroneos. [!]", \
        "=> Por favor, digita tu suma con [+] : ", "[!] = Sólo hay un valor para sumar, agrega más. o no estás usando el signo correcto [+]. [!]", "\n[!] El resultado de la suma es: ", \
            "\n=> Quieres hacer otra suma o ir al menú? [SUMA - MENU - SALIR] : ", "\n[!] = Gracias por usar la calculadora.   /  xKaaay. [!]\n"], \
    ["\n[!] Too many wrong attemps [!]\n", "=> Option: ", "\n                     [!] Please, select according to the menu. [!]\n", "                             [!] You've tried wrong values too many times. [!]", \
        "=> Please, type your addition with [+] : ", "[!] = There's only one digit, add more. or you're not using the right sign [+]. [!]", "\n[!] The total of the addition is: ", \
            "\n=> Wwant to do another addition or go to menu? [ADDITION - MENU - EXIT] : ", "\n[!] = Thanks for using the calculator.   /  xKaaay. [!]\n"]]


# Addition formula
def suma():
    global length
    global tries
    global exitc

    while length == False:
        tries += 1
        if tries > 3:
            print(l[lS][3])
            break

        var = input(l[lS][4])
        var = var.split("+")
        if "" in var:
            for i in range(var.count("")):
                var.remove("")


        if len(var) <= 1:
            print(l[lS][5])
            print(sep)
        else:
            res = 0
            for i in range(len(var)):
                op = int(var[i])
                res += op
            length = True
            print(sep)
            print(l[lS][6], res, " [!]\n")
            print(sep)
            exitm = input(l[lS][7])
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
                print(l[lS][8])
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
            [2] = Resta. [Aún no]
            [3] = Multiplicación. [Aún no]
            [4] = División. [Aún no]
            [5] = Salir. [Aún no]
            """)
        else: #If the user has chosen english
            print(""" 
            You've chosen english, these are the options:

            [1] = Addition.
            [2] = Substraction. [Not yet]
            [3] = Multiplication. [Not yet]
            [4] = Division. [Not yet]
            [5] = Exit. [Not yet]
            """)
        if tm > 3:
            clear()
            print(sep)
            print(l[lS][0])
            print(sep)
            break
        else:
            print(sep)
            opc = input(l[lS][1])
            opc = opc.lower()

            if opc == "suma" or opc == "1" or "suma" in opc or opc == "addition" or "addition" in opc:
                clear()
                suma()
            else:
                clear()
                print(sep)
                print(l[lS][2])
                exitc = 0

# First menu, select the language
while language == 0:
    language = 1
    print(sep)
    print("Select a language | Elije un idioma")
    print("""
    [1] = Español
    [2] = English [Not available yet]
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
        print("\n[!] Wrong command [!]\n")
        print(sep)
        break
