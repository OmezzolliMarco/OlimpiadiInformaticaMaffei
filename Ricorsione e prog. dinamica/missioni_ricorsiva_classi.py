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
    input()  # riga vuota / separatore
    D, S = map(int, input().strip().split())

    # inserire D ed S in una lista (ora di oggetti Missione)
    lista_missioni.append(Missione(D, S))


def calcola(idx, giorno):
    """
    Versione ricorsiva SENZA programmazione dinamica.
    Usa la lista globale 'lista_missioni'.

    idx   = indice della missione corrente
    giorno = tempo già occupato (somma durate missioni fatte finora)
    """
    N = len(lista_missioni)

    # caso base: abbiamo considerato tutte le missioni
    if idx == N:
        return 0

    m = lista_missioni[idx]  # missione corrente

    # Opzione 1: NON fare questa missione
    nonfatta = calcola(idx + 1, giorno)

    # Opzione 2: fare questa missione, se possibile
    fatta = 0
    if giorno + m.durata <= m.fine:
        fatta = 1 + calcola(idx + 1, giorno + m.durata)

    # ritorno il massimo tra fatta e nonfatta
    return fatta if fatta > nonfatta else nonfatta


# inserisci il codice qui
x = calcola(0, 0)
print(x)

sys.stdout.close()
