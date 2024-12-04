from votos1 import *
# Función para cargar las notas de los participantes
def cargar_notas(matriz):
    """Función para cargar las notas de tres jurados para cada participante.

    La función recorre la matriz de participantes y solicita a los usuarios
    que ingresen las notas (de 1 a 100) para cada jurado. Las notas se almacenan
    en las posiciones correspondientes de la matriz, asegurando que los valores
    estén dentro del rango válido (1-100).
    Args:
        matriz (list): Una lista de listas que representa la matriz de participantes,
                    donde cada sublista contiene el ID del participante seguido
                    de sus tres notas (inicializadas a 0).

    """
    for i in range(5):
        matriz[i][1] = int(input(f"Voto jurado 1 para participante {i+1} (1-100): "))
        #el otro ingresado se almacena en matriz i(el participante actual de 0 a 4, 1 es la segunda posicion de la sublista )
        # Verificar que el voto esté en el rango de 1 a 100
        while matriz[i][1] < 1 or matriz[i][1] > 100:
            print("Voto inválido. El voto debe estar entre 1 y 100.")
            matriz[i][1] = int(input(f"Voto jurado 1 para participante {i+1} (1-100): "))
        
        matriz[i][2] = int(input(f"Voto jurado 2 para participante {i+1} (1-100): "))
        while matriz[i][2] < 1 or matriz[i][2] > 100:
            print("Voto inválido. El voto debe estar entre 1 y 100.")
            matriz[i][2] = int(input(f"Voto jurado 2 para participante {i+1} (1-100): "))
        
        matriz[i][3] = int(input(f"Voto jurado 3 para participante {i+1} (1-100): "))
        while matriz[i][3] < 1 or matriz[i][3] > 100:
            print("Voto inválido. El voto debe estar entre 1 y 100.")
            matriz[i][3] = int(input(f"Voto jurado 3 para participante {i+1} (1-100): "))
def mostrar_votos(matriz):
    """Muestra una tabla con los votos de los participantes en tres turnos (mañana, tarde, noche)
    y su promedio.

    La función toma una matriz (lista de listas) que contiene los datos de cada participante, 
    incluyendo su ID y las notas de los tres jurados. Luego, muestra estos datos en una tabla
    de forma organizada, junto con el promedio de las tres notas del participante.

    Args:
        matriz (list): Una lista de listas donde cada sublista representa a un participante. 
                La sublista debe contener:
                - `matriz[i][0]`: El ID del participante.
                - `matriz[i][1]`: Nota del primer jurado (turno mañana).
                - `matriz[i][2]`: Nota del segundo jurado (turno tarde).
                - `matriz[i][3]`: Nota del tercer jurado (turno noche).
    """
    
    print("\n---------------------------------------------------------------------------") 
    print("| Nro lista | V- TURNO Mañana| V- TURNO Tarde | V- TURNO Noche | Promedio  |") 
    print("---------------------------------------------------------------------------")

    
    for i in range(len(matriz)):  
        promedio = calcular_promedio(matriz[i])# promedio de cada uno
        print(f"| {matriz[i][0]:<12} | {matriz[i][1]:<12} | {matriz[i][2]:<12} | {matriz[i][3]:<12} | {promedio:<10.2f} |")
        print("---------------------------------------------------------------------------")
# <12  Alinea el valor a la izquierda y asegura que ocupe un espacio mínimo de 12 caracteres.
#<10.2f: Alinea el valor a la izquierda y lo formatea como un número flotante con 2 decimales en un espacio mínimo de 10 caracteres.
