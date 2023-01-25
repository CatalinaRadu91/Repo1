
# Tema 4
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu

'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

# for
for i in range (0, len(masini)):
    print (f'Masina mea preferata este {masini[i]}')

# for each
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# while
i=0
masina = len(masini)
while i<masina:
    print(f'Masina mea preferata este {masini[i]}')
    i = i+1

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
2. Aceeași listă:
Folosește un for else
În for: Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
În else: Printează lista.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

# scriu toate elementele din lista cu majuscule:
    # masini_majuscule = [x.upper() for x in masini]
    # print(masini_majuscule)

# for else

for i in range(1, (len(masini)-1)):
    masini[i]=masini[i].upper()
else:
    print(masini)


for masina in masini:
    if masina in masini[1:-1]:
        masina.upper()
print(masini)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes. Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel: Printează ‘Am găsit mașina X. Mai căutam‘
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de Dumneavoastra.')
        break
    else:
      print(f'Am gasit masina {masina}. Mai cautam!')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
4. Aceași listă; Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
        continue
    else:
      print(f'S-ar putea sa va placa masina {masina}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

''' :(
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant: Salvează aceste mașini în masini_vechi. Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi = []

for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini.remove(masina)
        masini.append('Tesla')

print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
6. Având dict:

Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașinăxLastun
● Iterează prin listă.
'''
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(masina)

for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(masina,':', pret, 'euro')

for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina}.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
7. Având lista: numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    print(numar)

numar = 3
x = [i for i in numere if i ==numar]
print(x)

print(f'Numarul 3 apare de {len(x)} ori')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma = suma + numar
    print(f'Numarul este {suma}')
print (f'Suma numerelor este {suma}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar_maxim = 0

for numar in numere:
    if numar > numar_maxim:
        numar_maxim = numar
print(f'Numarul maxim este {numar_maxim}')


for i in range(len(numere)):
    if numere[i]>numar_maxim:
        numar_maxim = numere[i]
print(f'Numarul maxim este {numar_maxim}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă. (Ex: dacă e 3, să devină -3)
● Afișază noua listă.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for numar in range (0, len(numere)):
    if numere[numar] > 0:
        numere[numar] = numere[numar] * -1
print(numere)

# de ce nu functioneaza?

# for numar in numere:
#     if numar > 0:
#         numar = numar * (-1)
# print(numere)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

'''
1.
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

# for
for numar in range(0, len(alte_numere)):
    if alte_numere[numar] % 2 == 0:
        numere_pare.append(alte_numere[numar])
    elif alte_numere[numar] % 2 != 0:
        numere_impare.append(alte_numere[numar])
    if alte_numere[numar] > 0:
        numere_pozitive.append(alte_numere[numar])
    elif alte_numere[numar] < 0:
        numere_negative.append(alte_numere[numar])

print(f'Lista numerelor pare este {numere_pare}')
print(f'Lista numerelor impare este {numere_impare}')
print(f'Lista numerelor pozitive este {numere_pozitive}')
print(f'Lista numerelor negative este {numere_negative}')

# for each
# for numar in alte_numere:
#     if numar %2 ==0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar>=0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
#
# print(f'Lista numerelor pare este {numere_pare}')
# print(f'Lista numerelor impare este {numere_impare}')
# print(f'Lista numerelor pozitive este {numere_pozitive}')
# print(f'Lista numerelor negative este {numere_negative}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
2. Aceeași listă: Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici: https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_ordonate = []

i = 0
while len(alte_numere) > 0:
    numere_ordonate.append(min(alte_numere))
    alte_numere.remove(min(alte_numere))
    i = i+1
print(numere_ordonate)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while: User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''

import random
numar_secret = random.randint(1,30)
numar_ghicit = 0

while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Introdu un numar de la 1 la 30:'))
    if numar_ghicit < numar_secret:
        print(f'Numarul secret {numar_secret} este mai mare decat numarul ghicit {numar_ghicit}.')
    elif numar_ghicit > numar_secret:
        print(f'Numarul secret {numar_secret} este mai mic decat numarul ghicit {numar_ghicit}.')
print(f'Ai ghicit. Felicitari! Ai ales {numar_ghicit} si numarul secret a fost {numar_secret}.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

google: https://www.programiz.com/python-programming/examples/pyramid-patterns
'''

numar = int(input('Introdu un numar: '))
for i in range(numar+1):
    for y in range(i):
        print(i, end='')
    print('')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
5. Iterează prin listă 2d
Printează ‘Cifra curentă este x’ (hint: nested for - adică for în for)
'''

tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

for i in tastatura_telefon:
    for y in i:
        print(f'Cifra curentă este {y}')