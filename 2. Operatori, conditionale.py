# Tema 2 - Operatori, condiționale

'''
Exerciții Recomandate - grad de dificultate: Ușor

1. Revizualizează întâlnirea 2 și ia notițe în caz că ți-a scăpat ceva.

2. Vizualizează din ‘Primii pași în Programare’ video (Operatori și Flow Control). Link: https://www.itfactory.ro/8174437-intro-in-programare/
'''

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
Exerciții obligatorii - grad de dificultate: Ușor spre Mediu

# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare. Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe; X este un int.
'''

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
    # un if else este ca o intersectie de doua drumuri (doar pe unul putem merge); daca se indeplineste conditia, se alege primul drum, daca nu se indeplineste conditia, se alege al doilea drum.
    # if este urmat de conditie in timp ce else nu mai are nevoie de conditie

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 2. Verifică și afișează dacă x este număr natural sau nu.
# REFACUT # Denisa: considera si daca x nu e int !!! atunci cand se introduce de la tastatura, x va fi tot tp un string

# daca x nu este int
x = 2.5
if x >=0 and type(x) is int:
    print('Felicitari! Ai introdus un numar natural.')
else:
    print('Mai incearca! Numarul introdus nu este natural.')

# x este int
x = int(input('Introdu un numar natural: '))
if x>= 0:
    print('Felicitari! Ai introdus un numar natural')
else:
     print('Mai incearca! Numarul introdus nu este natural')

# daca x nu este int dar vreau sa introduc de la tastatura
x = input('Introdu un numar natural: ')
if x.isdigit():
    print('Felicitari! Ai introdus un numar natural')
else:
     print('Mai incearca! Numarul introdus nu este natural')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

x = int(input('Introdu un numar: '))

if x > 0 :
    print('Numarul introdus este pozitiv.')
elif x < 0:
    print('Numarul introdus este neagtiv.')
else:
    print('Numarul introdus este neutru.')

# x = int(input('Introdu un numar: '))
# if x>0:
#     print('Numarul introdus este pozitiv.')
# if x<0:
#     print('Numarul introdus este neagtiv.')
# if x==0:
#     print('Numarul introdus este neutru.')
# else:
#     pass

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 4.Verifică și afișează dacă x este între -2 și 13.
# REFACUT # Denisa: foloseste-te de formatarea care ti-o recomanda pycharm, sa lasi spatii in unele zone ca sa fie mai clar codul

# x = int(input('Introdu un numar: '))
# if -2 < x < 13:
#     print('Numarul se afla in intervalul (-2, 13)')
# else:
#     print ('Numarul nu se afla in intervalul (-2, 13)')

x = int(input('Introdu un numar: '))
if  x > -2 and x < 13:
    print('Numarul se afla in intervalul (-2, 13)')
else:
    print ('Numarul nu se afla in intervalul (-2, 13)')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5

x = int(input('Introdu un numar: '))
y = int(input('Introdu un alt numar: '))

if x-y<5:
    print('Diferenta dintre x si y este mai mica decat 5')
else:
    print('Diferenta dintre x si y nu este mai mica decat 5')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

x = int(input('Introdu un numar: '))

if not 5<x<27:
    print('Numarul introdus nu se afla intre 5 si 27')
else:
    print('Numarul introdus se afla intre 5 si 27')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 7. x și y (int). Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

x = int(input('Introdu un numar: '))
y = int(input('Introdu un alt numar: '))

if x==y:
    print('Cele doua numere introduse sunt egale.')
elif x>y:
    print(f'Primul numar introdus, {x}, este mai mare')
else:
    print (f'Al doilea numar introdus, {y}, este mai mare.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 8. x, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

x = int(input('Introdu valoarea laturei AB: '))
y = int(input('Introdu valoarea laturei BC: '))
z = int(input('Introdu valoarea laturei AC: '))

if x==y==z:
    print('Triunghiul este echilateral.')
elif x==y or x==z or z==y:
    print('Triunghiul este isoscel.')
else:
    print('Triunghiul nu este nici echilateral nici isoscel.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
# REFACUT : # Denisa: atentie, daca litera e majuscula?;  # Denisa: daca ai ales si varianta in care caracterul introdus nu e litera, poti avea mult mai multe variante decat numere

# litera = input('Intordu o litera:')
# if litera=='a' or litera=='e' or litera=='i' or litera=='o' or litera=='u':
#     print(f'Litera intodusa ({litera}) este o vocala.')
# else:
#     print(f'Litera introdusa ({litera}) este o consoana')

# litera = input('Intordu o litera:')
# if litera in ('a', 'e', 'i', 'o', 'u'):
#     print(f'Litera intodusa ({litera}) este o vocala.')
# elif litera in ('0', '1', '2','3', '4', '5','6', '7', '8', '9'):
#     print(f'Caracterul introdus ({litera}) nu este o litera. Reincercati.')
# else:
#     print(f'Litera introdusa ({litera}) este o consoana')

litera = input('Intordu o litera:').lower()

if litera in ('a', 'e', 'i', 'o', 'u'):
    print(f'Litera intodusa este o vocala.')
elif not (litera.isalpha()):
    print(f'Caracterul introdus nu este o litera. Reincercati.')
else:
    print(f'Litera introdusa este o consoana')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 10.Transformă și printează notele din sistem românesc în: Peste 9 => A, Peste 8 => B,, Peste 7 => C. Peste 6 => D, Peste 4 => E, 4 sau sub => F.

x= float(input('Introdu nota: '))

if x > 9:
    print('Ai luat nota A.')
elif 9 >= x > 8:
    print('Ai luat nota B.')
elif 8 >= x > 7:
    print('Ai luat nota C.')
elif 7 >= x > 6:
    print('Ai luat nota D.')
elif 6 >= x >4:
    print('Ai luat nota E.')
else:
    print('Ai luat nota F.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.

# 1.Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# DE REFACUT : # Denisa: si daca x e negativ?

x = input('Introdu un numar format din minim 4 cifre: ')

if len(x)>=4:
    print('Ai introdus un numar corect!')
else:
    print('Numarul introdus nu respecta conditia solicitata. Reincearca!')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 2. Verifică dacă x are exact 6 cifre

x = input('Introdu un numar format din 6 cifre: ')

if len(x)==6:
    print('Ai introdus un numar corect!')
else:
    print('Numarul introdus nu respecta conditia solicitata. Reincearca!')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3. Verifică dacă x este număr par sau impar (x e int).

x = int(input('Introdu un numar: '))

if x%2 == 0:
    print('Numarul introdus este par.')
else:
    print('Numarul introdus este impar.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 4. x, y, z (int). Afișează care este cel mai mare dintre ele?
# PROVOC: # Denisa: e corect; ca si provocare, incearca sa gasesti o functie care sa iti returneze cel mai mare nr

x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))
z = int(input('Introdu al treilea numar: '))

if (x>=y) and (x>=z):
    print(f'{x} este cel mai mare numar dintre cele trei numere introduse')
elif (y>=x) and (y>=z):
    print (f'{y} este cel mai mare numar dintre cele trei numere introduse')
else:
    print(f'{z} este cel mai mare numar dintre cele trei numere introduse')

print(f'{max(x,y,z)} este cel mai mare numar dintre cele trei numere introduse')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 5. x, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu
# REFACUT # Denisa: e suficienta conditia? Daca am un unghi de 0?
x = int(input('Introdu masura primului unghi: '))
y = int(input('Introdu masura celui de-al doilea unghi: '))
z = int(input('Introdu masura celui de-al treilea unghi: '))

if x + y + z == 180 and x != 0 and y != 0 and z != 0:
    print('Triunghiul este valid')
else:
    print('Triunghiul este invalid')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'.
    # Citiți de la tastatură un int x
    # Afișează stringul fără ultimele x caractere
    # Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

x= int(input('Introdu un numar: '))
prop = 'Coral is either the stupidest animal or the smartest rock'

print(prop[:-x])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 7.Același string. Declară un string nou care să fie format din primele 5 caractere  + ultimele 5

string = 'Coral is either the stupidest animal or the smartest rock'

string_1 = string[:5]
string_2 = string[-5:]
print(string_1 + string_2)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 8. Același string:
    # ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:este o funcție care te ajuta sa faci asta)
    # ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
    # ● output: 'Coral is either the stupidest animal or the smartest '

string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.rfind('rock')

final_string = print(string[:index_rock])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 9. Citește de la tastatura un string
    # Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
    # Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
# REFACUT : # Denisa: cel mai eficient e sa chemi o functie de cat mai putine ori

# string = input('Scrieti un cuvant:')
# primul_caracter = string[0]
# ultimul_caracter = string[-1]
# assert primul_caracter.lower() == ultimul_caracter.lower()
# print("Primul si ultimul carcater sunt la fel.")

assert str.lower(string[0]) == str.lower(string[-1]), "Primul si ultimul carcater nu sunt la fel."
print("Primul si ultimul carcater sunt la fel.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 10.Avand stringul '0123456789'
    # ● Afișați doar numerele pare
    # ● Afișați doar numerele impare
    # (hint: folositi slicing, controlați din pas)
# REFACUT # Denisa: daca preferi sa printezi direct, nu mai e nevoie sa salvezi valoarea intr-o variabila, daca oricum nu faci nimic cu ea dupa

# string ='0123456789'
# numere_pare= print(string[0::2])
# numere_impare= print(string[1::2])

string ='0123456789'
print(string[0::2])
print(string[1::2])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 11. Joc ghicit zarul. Caută pe net și vezi cum se generează un număr random. Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
    #Luați un numărul ghicit de la utilizator. Verificați și afișați dacă utilizatorul a ghicit. Veți avea 3 opțiuni
        # ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
        # ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
        # ● Ai ghicit. Felicitari! Ai ales x si zarul a fost Y

import random
dice_roll = random.randint(1,7)
print(dice_roll)
numar_ghicit = int(input('Introdu un numar de la 1 la 6:'))

if numar_ghicit < dice_roll:
    print (f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit} dar a fost {dice_roll}')
elif numar_ghicit > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {numar_ghicit} si zarul a fost {dice_roll}')