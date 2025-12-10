#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')


class Missione:
    def __init__(self, durata, fine):
        self.durata = durata  # D
        self.fine = fine      # S


T = int(input().strip())
lista_missioni = []

for test in range(1, T+1):
    input()  # riga vuota / separatore, come da template
    D, S = map(int, input().strip().split())

    # inserire D ed S in una lista (ora di oggetti Missione)
    lista_missioni.append(Missione(D, S))


# ------------------------------
#   PROGRAMMAZIONE DINAMICA
#   (ricorsione + dizionario)
# ------------------------------

N = len(lista_missioni)

# dizionario di memoization:
# chiave: (idx, giorno)
# valore: miglior numero di missioni da lì in poi
memo = {}


def calcola(idx, giorno):
    """
    Restituisce il numero massimo di missioni eseguibili
    a partire da missione idx, avendo già usato 'giorno'
    unità di tempo.
    """
    # se abbiamo già calcolato questo stato, riutilizza il risultato
    if (idx, giorno) in memo:
        return memo[(idx, giorno)]

    # caso base: finite le missioni
    if idx == N:
        memo[(idx, giorno)] = 0
        return 0

    m = lista_missioni[idx]

    # opzione 1: NON faccio questa missione
    best = calcola(idx + 1, giorno)

    # opzione 2: provo a farla, se riesco a finirla in tempo
    if giorno + m.durata <= m.fine:
        best = max(best,
                   1 + calcola(idx + 1, giorno + m.durata))

    # memorizzo il risultato prima di restituirlo
    memo[(idx, giorno)] = best
    return best


# inserisci il codice qui
x = calcola(0, 0)
print(x)

sys.stdout.close()
