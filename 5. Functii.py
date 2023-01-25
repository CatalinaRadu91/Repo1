
# Tema 5 - Funcții

# Exerciții obligatorii - grad de dificultate: Usor spre MediuExerciții obligatorii - grad de dificultate: Usor spre Mediu

# 1.Funcție care să calculeze și să returneze suma a două numere

#return
def suma_a_doua_numere (a,b):
    return(a+b)

print(suma_a_doua_numere(2, 7))

a = int(input('Introduceti primul numar:'))
b = int(input('Introduceti al doilea numar:'))
print(f'Suma celor doua numere {a} si {b} este {suma_a_doua_numere(a,b)}.')

#print
def suma_numere (a,b):
    print(a+b)

suma_numere(2, 3)
suma_numere(2, -1)
suma_numere(2.5, -1)

# ----------------------------------------------------------------------------------------------------------------------


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

# return
def numar_par (numar):
    if numar% 2 == 0:
        return True
    return False

# numar = int(input('Introduceti un numar: '))
# print(numar_par(numar))

print(numar_par(int(input('Introduceti un numar: ')))) #varianta simplificata pentru cele 2 randuri de mai sus

# print
def numar_par (numar):
    if numar% 2 == 0:
        print('TRUE')
    else:
        print('FALSE')

numar_par(int(input('Introduceti un numar: ')))


# ----------------------------------------------------------------------------------------------------------------------


# 3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

def numar_caractere(nume, prenume, nume_mijlociu = None):
    if nume_mijlociu == None:
        return len(nume) + len(prenume)
    else:
        return len(nume) + len(prenume) + len(nume_mijlociu)

print(numar_caractere('Radu', 'Catalina', 'Isabela'))
print(numar_caractere('Radu', 'Catalina'))


nume = input('Completati numele dvs: ')
prenume = input('Completati prenumele dvs: ')
nume_mijlociu = input('Completati numele mijlociu al dvs: ')

print(f'Numele dvs intreg este format din {numar_caractere(nume, prenume, nume_mijlociu)} caractere.')

# ----------------------------------------------------------------------------------------------------------------------


# 4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(L, l):
    return(L*l)

print(aria_dreptunghiului(2.3,5))

L = float(input('Introduceti lungimea dreptunghiului: \n'))
l = float(input('Introduceti latimea dreptunghiului: \n'))

print(f'Aria dreptunghiului este: {aria_dreptunghiului(L,l)} cm patrati.')

# ----------------------------------------------------------------------------------------------------------------------


# 5. Funcție care returnează aria cercului (A = π R²)

def aria_cercului (raza):
    return(3.14 * raza ** 2)

print(aria_cercului(3))

raza = float(input('Introdu raza cercului: '))
print(f'Aria cercului este {aria_cercului(raza)}')

# ----------------------------------------------------------------------------------------------------------------------


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

def gaseste_caracterul(caracter, string):
    if caracter.upper() in string.upper():
        return True
    return False

print(gaseste_caracterul('*', 'Xil*ofon'))
print(gaseste_caracterul('X', 'xilofon'))
print(gaseste_caracterul('a', 'xilofon'))

# or
def gasesteCaracterul (caract,str):
    for x in str:
        if x == caract:
            return True
        else:
            return False

caract = input('Introduceti caracterul pe care doriti sa-l cautati in cadrul stringului: ')
str = input('Introduceti un string: ')

print(gaseste_caracterul(caract, str))

# ----------------------------------------------------------------------------------------------------------------------


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def lower_upper(string):
    caractere_lower = 0
    caractere_upper = 0
    for caracter in string:
        if caracter.islower():
            caractere_lower += 1
        elif caracter.isupper():
            caractere_upper += 1
        else:
            pass
    print(f'Stringul introdus este: {string}')
    print(f'Numarul de caractere lower este {caractere_lower}')
    print(f'Numarul de caractere upper este {caractere_upper}')


lower_upper('Ana are Mere. Dana are Pere.')

# ----------------------------------------------------------------------------------------------------------------------


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

def lista_numere_pozitive(lista_numere):
    lista = []
    for numar in lista_numere:
        if numar>0:
            lista.append(numar)
        else:
            pass
    print(lista)

lista_numere = [-1, 10, 2.5, -7, 8, -100, -3.4, 0.5]
lista_numere_pozitive(lista_numere)

#-----------------------------------------------------------------------------------------------------------------------


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def compara_numere (numar1, numar2):
    # numar1 = int(input('Introdu un numar: '))
    # numar2 = int(input('Introdu al doilea numar: '))    # intrebare pentru DENISA:este in regula sa trec inputurile in cadrul functiei?
    if numar1 > numar2:
        print(f'Primul numar: {numar1}, este mai mare decat al doilea numar: {numar2}.')
    elif numar1 < numar2:
        print(f'Al doilea numar: {numar2}, este mai mare decat primul numar: {numar1}.')
    else:
        print('Numerele sunt egale.')

compara_numere(-4,-1)

numar1 = int(input('Introdu un numar: '))
numar2 = int(input('Introdu al doilea numar: '))
compara_numere(numar1, numar2)

# ----------------------------------------------------------------------------------------------------------------------


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

def set_nou (numar, set_numere):
    if numar in set_numere:
        print('Nu am adaugat numarul in set. Acesta exista deja.')
        return False
    else:
        set_numere.add(numar)
        print(f'Am adaugat numarul nou in set: {set_numere}')
        return True

set_nou(3, {3, 6, 0, 9})
set_nou(4, {10, 9, 6, 16, 100})

numar = 4.2
set_numere = {3, 2, 4.8, 5}
set_nou(numar,set_numere)

# ----------------------------------------------------------------------------------------------------------------------


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna.
def numar_zile_luna(luna):
    if luna.lower() == 'februarie':
        print(f'Luna {luna} anul acesta are 28 de zile.In anii bisecti, are 29 de zile.')
    elif luna.lower() == 'aprilie' or luna.lower() == 'iunie' or luna.lower() == 'septembrie' or luna.lower() == 'noiembrie':
        print(f'Luna {luna} are 30 de zile.')
    else:
        print(f'Luna {luna} are 31 de zile.')

numar_zile_luna('NOIEMBRIE')
numar_zile_luna('IANUARIE')

# ----------------------------------------------------------------------------------------------------------------------


#  2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

# NU STIU DACA AM INTELES OK CERINTA EXERCITIULUI :|

def calculator(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a, b, c, d

a,b,c,d = calculator(2, 5)

print('Suma: ', a)
print('Diferenta: ', b)
print('Inmultirea: ', c)
print('Impartirea: ', d)

# ----------------------------------------------------------------------------------------------------------------------

# !!!!!!!!!!!!!!!!
# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def contorizare_cifre(*cifre):
    dict = {}
    for cifra in range(0,10):
        dict[cifra] = cifre.count(cifra)
    return dict

print(contorizare_cifre(2, 3, 1, 4, 2, 9, 7, 7, 7))

# ----------------------------------------------------------------------------------------------------------------------


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

#var 1
def valoare_maxima(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(valoare_maxima(-2, -5, -1))

# var 2
def valoarea_max(x, y, z):
    for i in range(x, y, z):
        i = max(x, y, z)
        return i

print(valoarea_max(-2, 1, -7)) # de ce imi da None?
print(valoarea_max(20, 29, 30))

# ----------------------------------------------------------------------------------------------------------------------

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def suma_numerelor(numar):
    sum = 0
    for nr in range (0, numar+1):
        sum = sum + nr
    return sum

print(suma_numerelor(5))

# ----------------------------------------------------------------------------------------------------------------------


# Exerciții Opționale - Bonus

# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def numere_comune(lista1, lista2):
    common_list = set(lista1).intersection(lista2)
    return common_list

lista1 = [3, 4, 5, 2]
lista2 = [3, 10, 20, 1]
print(numere_comune(lista1,lista2))

# ----------------------------------------------------------------------------------------------------------------------


# 2. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.

def reducere_pret (pret, discount):
    if pret > 0 and discount <100:
        pret_redus = pret - (discount*pret/100)
        print(f'Produsul este la pretul redus de {pret_redus} lei')
    else:
        print(f'Reducere invalida. Mai incearca!')

reducere_pret(100,100)

# ----------------------------------------------------------------------------------------------------------------------

# 3. Funcție care să afișeze data și ora curentă din ro (bonus: afișați și data și ora curentă din China)
# NU STIU cum sa import datetime

def data_ora_RO():
    data_ora = datetime.now()


# ----------------------------------------------------------------------------------------------------------------------

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :
# am nevoie de datetime...