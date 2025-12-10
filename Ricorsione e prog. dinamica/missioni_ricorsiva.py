#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('Ricorsione e prog. dinamica\\input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
lista_missioni = []

for test in range(1, T + 1):
    D, S = map(int, input().strip().split())

    # inserire D ed S in una lista di tuple
    lista_missioni.append((D, S))


# -----------------------------------------------------
#   VERSIONE RICORSIVA SENZA PROGRAMMAZIONE DINAMICA
# -----------------------------------------------------

def calcola(missioni, N, idx, giorno):
    """
    missioni: lista di tuple (durata, fine)
    N: numero di missioni
    idx: indice della missione corrente
    giorno: tempo totale già usato
    """
    if idx == N:
        return 0

    durata, fine = missioni[idx]

    # Opzione 1: non faccio questa missione
    nonfatta = calcola(missioni, N, idx + 1, giorno)

    # Opzione 2: provo a farla
    fatta = 0
    if giorno + durata <= fine:
        fatta = 1 + calcola(missioni, N, idx + 1, giorno + durata)

    return fatta if fatta > nonfatta else nonfatta


# ora la ricorsione lavora su T missioni lette come tuple
N = len(lista_missioni)

# x è il risultato finale richiesto dal template
x = calcola(lista_missioni, N, 0, 0)

# output
print(x)

sys.stdout.close()
