import numpy as np

matriz = np.zeros((9, 9), dtype=int)

def imprimir_matriz(matriz):
     for i in range(9):
        for j in range(9):
            print(matriz[i][j], end=' ')
            
            if (j + 1) % 3 == 0 and j != 8:
                print('|', end=' ')
        
        print()  
        
        if (i + 1) % 3 == 0 and i != 8:
            print('-' * 21)

imprimir_matriz(matriz)
