import numpy as np
import random

def imprimir_matriz(tablero):
    print("    0 1 2 | 3 4 5 | 6 7 8")
    print("   ----------------------")
    for i in range(9):
        print(f"{i} | ", end='')  
        for j in range(9):
            valor = '-' if tablero[i][j] == 0 else tablero[i][j]
            print(valor, end=' ')
            if (j + 1) % 3 == 0 and j != 8:
                print('|', end=' ')
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("   ----------------------")

def es_valido(tablero, fila, col, num):
    if num in tablero[fila, :] or num in tablero[:, col]:
        return False

    start_row, start_col = 3 * (fila // 3), 3 * (col // 3)
    if num in tablero[start_row:start_row+3, start_col:start_col+3]:
        return False

    return True

def llenar_tablero_aleatorio(tablero):
    espacios_llenos = 0
    while espacios_llenos < 20: 
        fila = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if tablero[fila, col] == 0 and es_valido(tablero, fila, col, num):
            tablero[fila, col] = num
            espacios_llenos += 1
    return tablero

def sudoku_interactivo(tablero):
    while True:
        print()
        imprimir_matriz(tablero)

        continuar = input("\n¿Desea continuar? (s/n): ")
        if continuar.lower() == 'n':
            print("Juego terminado.")
            break

        try:
            fila = int(input("Ingrese la fila (0-8): "))
            columna = int(input("Ingrese la columna (0-8): "))
            numero = int(input("Ingrese el número (1-9): "))

            if 0 <= fila <= 8 and 0 <= columna <= 8 and 1 <= numero <= 9:
                if tablero[fila][columna] == 0 and es_valido(tablero, fila, columna, numero):
                    tablero[fila][columna] = numero
                else:
                    print("No se puede colocar el número en esa posición.")
            else:
                print("Entrada no válida, asegúrese de ingresar números en el rango permitido.")
        except ValueError:
            print("Entrada no válida. Ingrese números enteros.")

if __name__ == "__main__":
    matriz = np.zeros((9, 9), dtype=int)
    llenar_tablero_aleatorio(matriz)
    print("==========================================")
    print("Tablero de Sudoku generado para jugar:")
    sudoku_interactivo(matriz)
