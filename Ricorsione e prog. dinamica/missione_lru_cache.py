#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys
from functools import lru_cache

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

T = int(input().strip())
lista_missioni = []

for test in range(1, T+1):
    input()  # riga vuota / separatore, come da template
    D, S = map(int, input().strip().split())

    # inserire D ed S in una lista di tuple
    lista_missioni.append((D, S))   # (durata, fine)


N = len(lista_missioni)


@lru_cache(maxsize=None)
def calcola(idx, giorno):
    """
    Restituisce il numero massimo di missioni eseguibili
    a partire da missione idx, avendo già occupato 'giorno'
    giorni di lavoro.
    """
    # caso base: ho considerato tutte le missioni
    if idx == N:
        return 0

    durata, fine = lista_missioni[idx]

    # opzione 1: non faccio questa missione
    best = calcola(idx + 1, giorno)

    # opzione 2: provo a farla, se riesco a finirla entro 'fine'
    if giorno + durata <= fine:
        best = max(best,
                   1 + calcola(idx + 1, giorno + durata))

    return best


#inserisci il codice qui
x = calcola(0, 0)
print(x)

sys.stdout.close()
