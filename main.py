#!/usr/bin/python3
import matplotlib.pyplot as plt
import math
import csv

def distanciaEuclidiana(a, b):
    somaAtual = 0
    if len(a) == len(b):
        for i in range(len(a)):
            somaAtual += math.sqrt(math.pow(a[i] - b[i], 2))
    return somaAtual

def lerCSV(filename):
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        valores = list(spamreader)
    for r in valores:
        r = r[1:6]
        try:
            r = list(map(int, r))
        except Exception:
            for index, value in enumerate(r):
                if value == '?':
                    r[index] = 0
            r = list(map(int, r))
            pass
        print (r)
    return valores



def main():
    lista = lerCSV('breast-cancer-wisconsin.data')
    # for r in lista:



if __name__ == "__main__":
    main()