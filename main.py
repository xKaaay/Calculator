# Ended on 29/05/2022 - xKaaay - :)

#[do] Syntax listName[operation][language][position]
#[do], 0 = addition, 1 = subtract, 2 = multiplication, 3 = division.

#[lS] Syntax listName[langauge][position]
#[lS], 0 = Spanish, 1 = English

tries, exitc, language, do, length, sep, indexSubs = 0, 0, 0, 0, False, "-" * 80, False # This will be for later, don't ask why for :)

version = "/ Version = 1.0.1"
import re # for Curious people
import os # To clear the console
def clear():
    os.system('cls' if os.name=='nt' else 'clear') # This will work on Windows and Linux

# Cute title Owo
title = "<|>  xKaaay Calculator " + version + "  <|>"
print(title.center(80, " "))

# List of the variations depending on the language / [0] = Spanish, [1] = English)
l = [["\n[!] Demasiados intentos fallidos [!]\n", "=> Opción: ", "\n                     [!] Por favor, elije según el menú. [!]\n", "\n[!] Has intentado demasiadas veces valores erroneos. [!]\n", \
"=> Por favor, digita tu", "[!] = Sólo hay un valor para sumar, agrega más. o no estás usando el signo correcto", "\n[!] El resultado de la", \
"\n=> ¿Quieres hacer otra", "\n[!] = Gracias por usar la calculadora.   /  xKaaay. [!]\n"], \
    ["\n[!] Too many wrong attemps [!]\n", "=> Option: ", "\n                     [!] Please, select according to the menu. [!]\n", "\n[!] You've tried wrong values too many times. [!]\n", \
"=> Please, type your", "[!] = There's only one digit, add more. or you're not using the right sign", "\n[!] The total of the", \
"\n=> Want to do another", "\n[!] = Thanks for using the calculator.   /  xKaaay. [!]\n"]]

# Operations
o = [[["+", "suma"], ["+", "addition"]], \
        [["-", "resta"], ["-", "subtract"]], \
            [["*", "multiplicación"], ["*", "multiplication"]], \
                [["/", "división"], ["/", "division"]]]

# Variations
v = ["con", "es", "o ir al menú?", "salir"],\
    ["with", "is", "or go to menu?", "exit"]

# There are some people that just want the world burn
def Curious(listvar):
    listvar = re.sub("[,;.:_<>{^}´¨~¿¡'?)(&%$#!|°¬a'bcdefghijklmnopqrstuvwxyzñ ]","",listvar)
    return listvar

# Converting evetyrhing into a list to do the math
def split(vsplit):
    global indexSubs
    if "*" in vsplit:
        if vsplit.startswith("-") or "-" in vsplit:
            indexSubs = True

        vsplit = re.sub("[-+/]", "", vsplit)
        vsplit = vsplit.split("*")
    
    if "/" in vsplit:
        if "-" in vsplit:
            if vsplit.count("-") == 1 or vsplit.count("-") % 2 == 1:
                indexSubs = True

        vsplit = re.sub("[-+*]", "", vsplit)
        vsplit = vsplit.split("/")

    if "+" in vsplit:
        vsplit = re.sub("[-/*]", "", vsplit)
        vsplit = vsplit.split("+")
    
    if "-" in vsplit:
        vsplit = re.sub("[*+/]", "", vsplit)
        if vsplit.startswith("-") or "-" in vsplit[0]:
            indexSubs = True
        vsplit = vsplit.split("-")

    if type(vsplit) is not list:
        return [vsplit]
    else:
        return vsplit

def dothemath():
    global length, tries, exitc

    while length == False:
        tries += 1 
        if tries > 3: # We don't want an infinite loop
            clear()
            print(sep + "\n" + l[lS][0] + "\n" + sep)
            break

        var = input(f"{l[lS][4]} {o[do][lS][1]} {v[lS][0]} [{o[do][lS][0]}]: ") # Please, type your [do] [variation] [sign].
        var = Curious(var)
        var = split(var)

        if len(var) <= 1:
            print(f"{l[lS][5]} [{o[do][lS][0]}] [!]") # There's only one digit, add more. or you're not using the right sign [do].
            print(sep)

        else:
            if "" in var:
                for i in range(var.count("")):
                    var.remove("")
            res = 0
            if do == 0: # if do = addition
                for i in range(len(var)):
                    op = int(var[i])
                    res += op

            elif do == 1: # if do = subtract
                for i in range(len(var)):
                    if indexSubs: #check if the subtract starts with -
                        op = int(var[i])
                        res -= op
                    else:
                        op = int(var[i])
                        res = int(var[0])
                        res -= op
            if do == 2: # if do = multiplication
                if indexSubs:
                    res = -1
                else:
                    res = 1
                for i in range(len(var)):
                    op = int(var[i])
                    res *= op
            if do == 3: # if do = division
                if indexSubs:
                    res = int(var[0]) / -1
                else:
                    res = int(var[0]) / 1
                for i in range(1, len(var)):
                    op = int(var[i])
                    res /= op

            length = True # Break the loop

            print(sep)
            print(f"{l[lS][6]} {o[do][lS][1]} {v[lS][1]}: {res}  [!]\n") # The total of the [do] [variation].
            print(sep)
            exitm = input(f"{l[lS][7]} {o[do][lS][1]} {v[lS][2]} [{o[do][lS][1].upper()} - MENU - {v[lS][3].upper()}]: ") # Want to do another [do] or go to menu? [[do] - MENU - [EXIT]].
            exitm = exitm.lower()

            if exitm == o[do][lS][1] or o[do][lS][1] in exitm or exitm == "1":
                print("\n", sep)
                tries, length = 0, False

            elif exitm == "menu" or "menu" in exitm or "menú" in exitm or exitm == "2":
                clear()
                tries, length, exitc = 0, False, 0 # Reactivate the loop
                break
            else:
                print("\n", sep)
                print(l[lS][8]) # Thanks for using the calculator.
                print(sep)
                break

# Second menu with all the options available
def menu():
    global length, tries, exitc, do
    while exitc == 0:
        tries += 1
        exitc = 1 # Break the loop
        print(sep)
        if lS == 0:  #If the user has chosen spanish
            print(""" 
            Elegiste español, estas son las opciones:

            [1] = Suma.
            [2] = Resta.
            [3] = Multiplicación.
            [4] = División.
            [5] = Salir.
            """)
        else: #If the user has chosen english
            print(""" 
            You've chosen english, these are the options:

            [1] = Addition.
            [2] = Subtraction.
            [3] = Multiplication.
            [4] = Division.
            [5] = Exit.
            """)
        if tries > 3: # We don't want an infinite loop
            clear()
            print(sep + "\n" + l[lS][0] + "\n" + sep)
            break
        else:
            print(sep)
            opc = input(l[lS][1]) # [1] = Option:
            opc = opc.lower()

            if opc == "1" or o[0][0][1] in opc or o[0][1][1] in opc:
                clear()
                tries = 0
                dothemath()
            elif opc == "2" or o[1][0][1] in opc or o[1][1][1] in opc:
                clear()
                do, tries = 1, 0
                dothemath()
            elif opc == "3" or o[2][0][1] in opc or o[2][1][1] in opc:
                clear()
                do, tries = 2, 0
                dothemath()
            elif opc == "4" or o[3][0][1] in opc or o[3][1][1] in opc:
                clear ()
                do, tries = 3, 0
                dothemath()
            elif opc == "salir" or "salir" in opc or opc == "5" or opc == "exit" or "exit" in opc:
                clear()
                print("\n" + sep)
                print(l[lS][8]) # [8] = Thanks for using the calculator.
                print(sep)
                break
            else:
                clear()
                print(sep)
                print(l[lS][2]) # [2] = Please, select according to the menu.
                exitc = 0 # Reactivate the loop


# First menu, selecting the language
while language == 0:
    tries += 1
    language = 1
    print(sep)
    print("""
    Select a language | Elije un idioma

    [1] = Español
    [2] = English
    """)

    if tries > 3: # We don't want an infinite loop
        clear()
        print(sep + "\n" + l[lS][0] + "\n" + sep)
        exit()

    print(sep)
    langSel = input("=> ")
    langSel = langSel.lower()
    if langSel == "1" or langSel == "español" or "español" in langSel:
        lS, tries = 0, 0
        clear(), menu()
    elif langSel == "2" or langSel == "english" or "english" in langSel:
        lS, tries = 1, 0
        clear(), menu()
    else:
        clear()
        print(sep + "\n   [!] Wrong command / Comando erroneo[!]\n")
        language = 0
