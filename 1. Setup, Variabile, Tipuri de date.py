
#Tema 1 _ Setup, Variabile, Tipuri de date

# 1. Revizualizează întâlnirea 1 și ia notițe în caz că ți-a scăpat ceva.

# 2. Vizualizează din videoul Primii pași în Programare: Variabile și Tipuri; Operatori și Flow Control.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# O variabila este o zona din memoria unui calculator care tine date; o cutiuta pe care punem o eticheta si in care punem valori

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă : string, int, float, bool. Observație: Valorile vor fi alese de tine după preferințe.

produs = 'crema de fata'
cantitate = 10
pret = 70.50
stoc_disponibil = True

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(produs)) # <class 'str'>
print(type(cantitate)) # <class 'int'>
print(type(pret)) # <class 'float'>
print(type(stoc_disponibil)) # <class 'bool'>

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere). Verifică tipul acesteia.

pret = round(pret)
print(pret)
print(type(pret))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile. Rezolvă nepotrivirile de tip prin ce modalitate dorești.

# Prop 1: Avem de onorat o comanda de 10 bucati de crema de fata la pretul de 70 lei.
print(f'Avem de onorat o comanda de {cantitate} bucati de {produs} la pretul de {pret} lei.')
print('Avem de onorat o comanda de '+str(cantitate)+' bucati de '+produs+' la pretul de '+str(pret)+' lei.')


# Prop 2: Pretul de 70 lei se aplica si daca cumpar 10 bucati de crema de fata la o singura comanda?
print(f'Pretul de {pret} lei se aplica si daca cumpar {cantitate} bucati de {produs} la o singura comanda?')
print('Pretul de '+str(pret)+' lei se aplica si daca cumpar '+str(cantitate)+' bucati de '+produs+' la o singura comanda?')

# Prop 3: Daca vreau sa cumpar mai mult de 10 bucati de crema de fata, pretul de 10 lei se pastreaza? Adevarat!
print(f'Daca vreau sa cumpar mai mult de {cantitate} bucati de {produs}, pretul de {pret} lei se pastraza? {stoc_disponibil}!')
print('Daca vreau sa cumpar mai mult de ' +str(cantitate)+ ' bucati de ' +produs+ ', pretul de ' +str(pret)+ ' se pastreaza? ' +str(stoc_disponibil)+ '!')

# Prop 4: Cate bucati de crema de fata mai avem pe stoc si la ce pret? 10 bucati la pretul de 70 lei!
print(f'Cate bucati de {produs} mai avem pe stoc si la ce pret? {cantitate} bucati la preul de {pret} lei!')
print('Cate bucati de ' +produs+ ' mai avem pe stoc si la ce pret? ' +str(cantitate)+ ' bucati la pretul de ' +str(pret)+ ' lei!')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 6. Citește de la tastatură: numele, prenumele. Afișează: 'Numele complet are x caractere'.

numele = input('Noteaza-ti numele: ')
prenumele = input ('Noteaza-ti prenumele: ')

nume_complet = numele + prenumele

print(f'Numele complet are {len(nume_complet)} caractere.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 7. Citește de la tastatură: lungimea, lățimea. Afișează: 'Aria dreptunghiului este x'.

lungimea = input('Introdu lungimea: ')
latimea = input('Introdu latimea: ')

aria_dreptunghiului = float(lungimea) * float(latimea)

print(f'Aria dreptunghiului este {aria_dreptunghiului}.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock'. Afișează de câte ori apare cuvântul 'the';

propozitie = 'Coral is either the stupidest animal or the smartest rock'
afisare_cuvant = propozitie.count(' the ')

print(f'Cuvantul "the" este afisat de {afisare_cuvant} ori.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 9. Același string. Inlocuieste "the" cu "THE" peste tot.

print(propozitie.replace('the', 'THE')) # Coral is eiTHEr THE stupidest animal or THE smartest rock

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 10. Același string. Folosiți un assert ca să verificați dacă acest string conține doar numere.

# assert propozitie.isdigit(), 'Stringul nu contine doar numere!'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Tema 1 - Optional

 # 1. ??? Citește de la tastatură un string de dimensiune impară. Afișează caracterul din mijloc.

cuvant = input('Introdu un string de dimensiune impara: ')

middle = cuvant[len(cuvant)//2]
print(f'Caracterul din mijloc este: {middle}');

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 2.  Folosind assert, verifică dacă un string este palindrom (supus)

string = input('Introdu un palindrom: ')

# def estePalindrom(string):
#     return string == string [::-1]
# rasp = estePalindrom(string)
# if rasp:
#     print('Este palindrom')
# else:
#     print ('Nu este palindrom')

assert string == string [::-1]
print ('Este palindrom')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3. ??? Folosind cat mai putine linii de cod:
    # - citește un string de la tastatură (ex: 'alabala portocala');
    # - salvează fiecare cuvânt într-o variabilă;
    # - printează ambele variabile pentru verificare.


# \n is a type of escape character that will create a new line when used.
string1, string2 = input('Noteza doua cuvinte: ').split(); print(string1, "\n", string2)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 4.  COPIAT!!!!  Citește un string de la tastatură (ex: alabala portocala);
    # salvează primul caracter într-o variabilă - indiferent care este el;
    # - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
    # caracter => alAbAlA portocAla.

string3 = input('Intodu 3 cadouri pe care ti le doresti de Craciun: ')
variabila1 = string3[0]
print (f'{variabila1}')

text, xlow = string3[1:-1], string3.lower ()
first, last = xlow [0], xlow[-1]

print(f'{first}{text.replace(first, first.upper())}{last}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 5. Citește un user de la tastatură;
    # - citește o parolă;
    # - afișează: 'Parola pt user x este ***** și are x caractere';
    # - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

user = input('User: ')
parola = input('Parola: ')

lungime_parola = len(parola)
afisare_parola = lungime_parola * '*'
print(f'Parola pentru user {user} este {afisare_parola} si are {lungime_parola} caractere.')
