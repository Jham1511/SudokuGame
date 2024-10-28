import numpy as np
import random

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
def es_valido(tablero, fila, col, num):
    """Verifica si un número puede ser colocado en la posición dada sin violar las reglas del Sudoku."""
    if num in tablero[fila, :] or num in tablero[:, col]:
        return False
    
    start_row, start_col = 3 * (fila // 3), 3 * (col // 3)
    if num in tablero[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

def llenar_tablero_aleatorio(tablero):
    intentos = 0
    while intentos < 20:  
        fila = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if tablero[fila, col] == 0 and es_valido(tablero, fila, col, num):
            tablero[fila, col] = num
            intentos += 1
    return tablero

llenar_tablero_aleatorio(matriz)
imprimir_matriz(matriz)
