from matriz import*
from votos1 import *
from ordenar import*
def mostrar_menu():
    """Menu de opciones
    """
    
    
    matriz= inicializar_matriz()
    notas_cargadas= False

    while True:
        
        print("\n--- Menú de opciones ---")
        print("1. Cargar notas de los participantes")
        print("2. Mostrar votos y promedios")
        print("3. Ordenar por promedio")
        print("4. Mostrar los peores 3 participantes")
        print("5. Mostrar participantes con promedio superior al promedio total")
        print("6. Jurado que puso la peor nota")
        print("7. Ingrese un numero, puede que coincida con la suma de sus tres notas. ")
        print("8. Determinar el ganador")
        print("9. Salir")
        
        opcion = input("Elija una opción (1-9): ")

        if opcion == '1':
            cargar_notas(matriz)
            notas_cargadas = True  # Se establecen las notas como cargadas
        elif opcion == '2':
            if notas_cargadas:
                mostrar_votos(matriz)
            else:
                print("Por favor, cargue las notas primero antes de mostrar los votos.")
        elif opcion == '3':
            if notas_cargadas:
                ordenar_por_promedio(matriz)
            else:
                print("Por favor, cargue las notas primero antes de ordenar.")
        elif opcion == '4':
            if notas_cargadas:
                buscar_peores_3(matriz)
            else:
                print("Por favor, cargue las notas primero antes de buscar los peores.")
        elif opcion == '5':
            if notas_cargadas:
                buscar_mayores_que_promedio_total(matriz)
            else:
                print("Por favor, cargue las notas primero antes de realizar esta búsqueda.")
        elif opcion == '6':
            if notas_cargadas:
                buscar_jurado_peor_nota(matriz)
            else:
                print("Por favor, cargue las notas primero antes de mostrar los votos.")
        elif opcion == '7':
            if notas_cargadas:
                buscar_por_suma(matriz)
            else:
                print("Por favor, cargue las notas primero antes de mostrar los votos.")
            
        elif opcion == '8':
            if notas_cargadas:
                definir_ganador(matriz)
            else:
                print("Por favor, cargue las notas primero antes de determinar al ganador.")
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
# Ejecutar el programa
mostrar_menu()



