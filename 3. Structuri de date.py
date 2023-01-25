
# Tema 3 - Structuri de date

'''
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 3 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video (Structuri de date, Flow Control)
Link: https://www.itfactory.ro/8174437-intro-in-programare/
'''

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Exerciții obligatorii - grad de dificultate: Usor spre Mediu

'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do: 
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă
● Printează varianta actuală (inversată)
● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea (nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat).
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

lista_note = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(lista_note)

lista_note_inversata = lista_note[::-1]
print(lista_note_inversata)

lista_note_inversata.reverse()
print(lista_note_inversata)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

lista_note = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
x= lista_note.count('do')
print(f'In lista de note, "do" apare de {x} ori')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4], găsește 2 variante să le unești într-o singură listă.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
print(lista3)

lista1.extend(lista2)
print(lista1)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sterge numărul 0 din lista folosind o funcție.
● Afișaza din nou lista.
'''

lista3.sort()
print(lista3)

lista3.pop(0)
print(lista3)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază pe fiecare ramura urmatoarele:
● Lista este goală (IF)
● Lista nu este goală (ELSE)
'''

lista3 = [3, 1, 0, 2, 6, 5, 4]
if len(lista3) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 6. Folosește o funcție care să goleasca lista de la exercițiul 3.

    # - am folosit metoda clear(); aceasta metoda doar goleste lista, nu o sterge complet
lista3.clear()
print(lista3)

    # - functia del sterge complet lista dar la printare genereaza o eroare deoarece lista nu mai exitsa
# del lista3
# print(lista3)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui să se afișeze că lista e goală.

if len(lista3) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
elevi = dict1.keys()
print(elevi)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor. Ex: ‘Ana a luat nota {x}’. Doar nota o vei lua folosindu-te de cheie.

dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
print(f'Ana a luat nota {dict1["Ana"]}.')
print(f'Gigel a luat nota {dict1["Gigel"]}.')
print(f'Dorel a luat nota {dict1["Dorel"]}.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


''' 
10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel'] = 6
print(f'Dupa contestatie, Dorel a luat nota {dict1["Dorel"]}.')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''
11. Imagineaza-ti ca Gigel se transfera din clasa.
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugati-l in lista pe Ionica, cu nota 9
● Printati dictionarul cu noii elevi
'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1.pop('Gigel')
print(dict1)
dict1['Ionica']= 9
print(dict1)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''
12. Ai urmatoarele seturi:
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
● Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
print(zile_sapt)
weekend = {'sâmbăta', 'duminică'}
print(weekend)

zile_sapt.add('luni')
print(zile_sapt)  # structurile de date de tip set nu pot contine 2 item-uri cu aceeasi valoare; valorile duplicate sunt ignorate

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se regasesc intre elementele din setul zile_sapt)
● Weekend nu este un subset al zilelor din săptămânii 
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui punct de mai sus va fi un boolean
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

if 'sâmbăta' and 'duminică' in zile_sapt:
    print("Weekend este un subset al zilelor din săptămână.")
else:
    print("Weekend nu este un subset al zilelor din săptămână.")


if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămână.")
else:
    print("Weekend nu este un subset al zilelor din săptămână.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 14. Afișează diferențele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

print(zile_sapt.difference(weekend))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 15. Afișază intersecția elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi). Hint: Va puteti folosi de o functie

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

print(zile_sapt.intersection(weekend))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
'''
Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.

● Declară o Listă cu 5 jucători: lista_jucatori_teren
● Declară o Listă cu 5 jucatori de rezerva: lista_jucatori_rezerva
● Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
● Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
● SCHIMBARI_MAX va fi o constanta cu valoarea 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele variabilelor voastre)

Dacă jucătorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’. Altfel, afisati ecran: ‘mai aveti z schimbari’

Google search hint: “how to check if item is în list python"

'''

lista_jucatori_teren = ['Tudor', 'Stefan', 'Darius', 'Tiberiu', 'Matei']
lista_jucatori_rezerva = ['Casian', 'Ianis', 'Ciprian', 'Cristian', 'Oleg']
lista_jucatori_scosi = []
Schimbari_efectuate = 0
SCHIMBARI_MAX = 3
Schimbari_ramase = SCHIMBARI_MAX - Schimbari_efectuate

jucator_schimbat = input('Introdu numele jucatorului care se doreste a fi schimbat: ')
noul_jucator = input('Introdu numele noului jucator din lista de jucatori de rezerva: ')

if jucator_schimbat in lista_jucatori_teren and noul_jucator in lista_jucatori_rezerva and noul_jucator not in lista_jucatori_teren and Schimbari_ramase > 0:
    lista_jucatori_teren.remove(jucator_schimbat)
    lista_jucatori_scosi.append(jucator_schimbat)
    lista_jucatori_teren.append(noul_jucator)
    lista_jucatori_rezerva.remove(noul_jucator)
    Schimbari_efectuate = Schimbari_efectuate+1
    print(f'A intrat {noul_jucator}, a iesit {jucator_schimbat}. Mai aveti {Schimbari_ramase} schimbari.')
elif noul_jucator not in lista_jucatori_rezerva or noul_jucator in lista_jucatori_teren:
    print(f'Nu se poate efectua schimbarea deoarece jucătorul {noul_jucator} nu se regaseste in lista jucatorilor de rezerva sau este deja in teren.')
    print(f'Mai aveti {Schimbari_ramase} schimbari.')
elif Schimbari_ramase == 0:
    print ('Nu mai pot fi efectuate schimbari!')
else:
    print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_schimbat} nu e în teren.')
    print(f'Mai aveti {Schimbari_ramase} schimbari.')

print(lista_jucatori_teren)
print(lista_jucatori_rezerva)
print(lista_jucatori_scosi)