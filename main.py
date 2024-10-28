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

def sudoku_interactivo(tablero):
    while True:
        imprimir_matriz(matriz)
        print("\nIngrese 'salir' en cualquier momento para finalizar.")
        
        entrada = input("Ingrese la fila (1-9), columna (1-9) y número (1-9) separados por espacios (ejemplo: '1 2 5'): ")
        if entrada.lower() == 'salir':
            print("Juego terminado.")
            break
        
        



if __name__ == "__main__":
    llenar_tablero_aleatorio(matriz)

    print("Tablero de Sudoku generado para jugar:")
    sudoku_interactivo(matriz)
