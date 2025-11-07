#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('Greedy\\input.txt')
#sys.stdout = open('output.txt', 'w')

T = int(input().strip())
lista_coppie = []
for test in range(1, T+1):
    N, M = map(int, input().strip().split())

    lista_coppie.append((N, M))

    print(lista_coppie)


x = 0
#codice qui

#ordino per secondo elemento
lista_coppie.sort(key=lambda x:x[1])

fine = lista_coppie[0][1]
caramelle = 1

for inizio, finale in lista_coppie[1:]:
    if fine < inizio:
        caramelle += 1
        fine = finale

print(lista_coppie)

print("Case #%d: " % test, end='')
print(caramelle)

sys.stdout.close()
