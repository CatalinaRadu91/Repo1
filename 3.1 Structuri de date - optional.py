'''
Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3

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

schimbari_efectuate = 0
SCHIMBARI_MAX = 3


while SCHIMBARI_MAX-schimbari_efectuate != 0:
    jucator_scos = input('Introdu numele jucatorului care se doreste a fi schimbat: ').capitalize()
    if jucator_scos in lista_jucatori_teren:
        jucator_nou = input('Introdu numele noului jucator din lista de jucatori de rezerva: ').capitalize()
        if jucator_nou in lista_jucatori_rezerva and jucator_nou not in lista_jucatori_teren:
            lista_jucatori_teren.remove(jucator_scos)
            lista_jucatori_teren.append(jucator_nou)
            lista_jucatori_rezerva.remove(jucator_nou)
            lista_jucatori_scosi.append(jucator_scos)

            schimbari_efectuate = schimbari_efectuate+1

            print(f'A intrat {jucator_nou}, a iesit {jucator_scos}. Mai aveti {SCHIMBARI_MAX - schimbari_efectuate} schimbari.')
        else:
            print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_nou} nu e în lista de rezerva.')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_scos} nu e în teren.')
        print(f'Mai aveti {SCHIMBARI_MAX - schimbari_efectuate} schimbari.')
print('Numarul maxim de schimbari a fost atins. Nu mai pot fi efectuate schimbari!')

print(lista_jucatori_teren)
print(lista_jucatori_rezerva)
print(lista_jucatori_scosi)