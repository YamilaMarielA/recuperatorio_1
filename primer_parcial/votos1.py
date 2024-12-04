
def calcular_promedio(participante):
    """Calcula el promedio de las tres notas dadas a un participante por los tres jurados.

    Esta función toma como entrada una sublista que representa a un participante. 
    La sublista contiene el ID del participante seguido de tres notas de jurados. 
    La función calcula el promedio de las tres notas y lo devuelve.

    Args:
    participante (list): Una sublista que representa a un participante. Esta sublista debe
                        contener, en las siguientes posiciones:
                        - `participante[0]`: ID del participante.
                        - `participante[1]`: Nota del primer jurado.
                        - `participante[2]`: Nota del segundo jurado.
                        - `participante[3]`: Nota del tercer jurado.

    Retuns:
    float: El promedio de las tres notas dadas por los jurados al participante.
    """
    return (participante[1] + participante[2] + participante[3]) / 3
    #los datos del participante (su ID y las tres notas de los jurados se dividen por la cantidad total de jurados)



def ordenar_por_promedio(matriz):
    """Busca y muestra los 3 peores participantes según el promedio de sus notas.

    Args:
        matriz (list): Una lista de listas donde cada sublista representa un participante. 
                    Cada sublista debe contener:
                    - `matriz[i][0]`: El ID del participante.
                    - `matriz[i][1]`: Nota del primer jurado (turno mañana).
                    - `matriz[i][2]`: Nota del segundo jurado (turno tarde).
                    - `matriz[i][3]`: Nota del tercer jurado
    """
    orden = input("¿Orden ascendente o descendente? (asc/desc): ")
    for i in range(5): 
        for j in range(i + 1, 5): #compara el participante actual, con el sigiuiente
            promedio_i = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
            #promedio de las notas del participante i (notas en las posiciones 1 , 2,3)
            promedio_j = (matriz[j][1] + matriz[j][2] + matriz[j][3]) / 3
            #es el promedio de las notas del participantes
            if (orden == "asc" and promedio_i > promedio_j) or (orden == "desc" and promedio_i < promedio_j):
                matriz[i], matriz[j] = matriz[j], matriz[i]
            #se realiza el intercambio si promedio i es promedio j. desc al reves.
            

    # Mostrar los participantes después del ordenamiento
    for i in range(5):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        print(f"Participante {matriz[i][0]}: {matriz[i][1]}, {matriz[i][2]}, {matriz[i][3]}, Promedio: {promedio:.2f}")
        #se recorre nuevamente la lista en el nuevo orden y se imprime


def buscar_peores_3(matriz):
    """Busca y muestra los tres peores participantes según el promedio de sus notas, 
    después de ordenar la lista de participantes por su promedio en orden ascendente.
    
    La función utiliza el algoritmo de ordenamiento por burbuja para ordenar los 
    participantes según sus promedios y luego imprime los tres primeros participantes 
    con los promedios más bajos.

    Args:
        matriz (list): Una lista de listas, donde cada sublista representa a un participante y contiene lo siguiente:
                    - matriz[i][0]: ID del participante.
                    - matriz[i][1]: Nota del primer jurado (turno mañana).
                    - matriz[i][2]: Nota del segundo jurado (turno tarde).
                    - matriz[i][3]: Nota del tercer jurado (turno noche)
    """
    
    for i in range(5):
        for j in range(i + 1, 5):
            promedio_i = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
            promedio_j = (matriz[j][1] + matriz[j][2] + matriz[j][3]) / 3
            if promedio_i > promedio_j:
                matriz[i], matriz[j] = matriz[j], matriz[i]

    print("Los 3 peores participantes:")
    for i in range(3):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        print(f"Participante {matriz[i][0]}: {matriz[i][1]}, {matriz[i][2]}, {matriz[i][3]}, Promedio: {promedio:.2f}")


def buscar_mayores_que_promedio_total(matriz):
    """Esta función calcula el promedio total de los participantes y luego muestra aquellos
    cuyo promedio de notas es superior al promedio total.

    El promedio total es el promedio de todos los promedios individuales de los participantes.
    Luego, se imprime la información de cada participante cuyo promedio individual supera
    el promedio total.

    Args:
        matriz (list): Una lista de listas, donde cada sublista representa a un participante.
                    La sublista debe tener la siguiente estructura:
                    - `matriz[i][0]`: ID del participante (entero).
                    - `matriz[i][1]`: Nota del primer jurado (entero).
                    - `matriz[i][2]`: Nota del segundo jurado (entero).
                    - `matriz[i][3]`: Nota del tercer jurado (entero).
    """
    total_promedio = 0
    for i in range(5):
        total_promedio += (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3 #se suman los promedios,
    promedio_total = total_promedio / 5 #promedio total
    print(f"Promedio total: {promedio_total:.2f}")


    print("Participantes con promedio superior al promedio total:")
    for i in range(5):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        if promedio > promedio_total:
            print(f"Participante {matriz[i][0]}: {matriz[i][1]}, {matriz[i][2]}, {matriz[i][3]}, Promedio: {promedio:.2f}")


def buscar_jurado_peor_nota(matriz):
    """Busca y muestra la peor nota entre todos los participantes y el jurado que la asignó.
    
    La función recorre todos los participantes y sus notas, y luego muestra la peor nota
    de entre todas, junto con el ID del participante y el jurado que la dio.

    Args:
        matriz (list of list): Una lista de 5 participantes, donde cada participante es una lista que contiene:
            - `matriz[i][0]`: ID del participante (int)
            - `matriz[i][1]`: Nota del primer jurado (int)
            - `matriz[i][2]`: Nota del segundo jurado (int)
            - `matriz[i][3]`: Nota del tercer jurado (int)
    """
    peor_nota = 101  # Inicializamos con un valor mayor que el máximo posible de nota (100)
    participante_peor = None
    jurado_peor = None
    
    # Recorremos cada participante y sus tres notas
    for i in range(5):
        for j in range(1, 4):  # Recorremos las notas de cada jurado (posiciones 1, 2, 3)
            if matriz[i][j] < peor_nota:
                peor_nota = matriz[i][j]
                participante_peor = matriz[i][0]  # Guardamos el ID del participante
                jurado_peor = j  # Guardamos el número del jurado que dio la peor nota

    # Asignamos el nombre del jurado según el número
    if jurado_peor == 1:
        jurado = "Jurado 1 (Mañana)"
    elif jurado_peor == 2:
        jurado = "Jurado 2 (Tarde)"
    else:
        jurado = "Jurado 3 (Noche)"

    # Mostramos la peor nota, el participante y el jurado correspondiente
    print(f"Participante {participante_peor} recibió la peor nota: {peor_nota} - {jurado}")
def buscar_por_suma(matriz):
    # Pedir el número entre 3 y 300
    while True:
        numero = int(input("Ingrese un número entre 3 y 300: "))
        if 3 <= numero <= 300:
            break
        else:
            print("Por favor, ingrese un número válido entre 3 y 300.")
    
    # Inicializamos una lista para almacenar los participantes con la suma correcta
    encontrados = []

    # Iterar sobre cada participante
    for participante in matriz:
        suma = participante[1] + participante[2] + participante[3]  # Sumar las tres notas

        # Verificar si la suma de las notas es igual al número ingresado
        if suma == numero:
            encontrados.append(participante)

    # Si encontramos participantes con la suma correcta, los mostramos
    if encontrados:
        print(f"Participantes cuya suma de notas es {numero}:")
        for participante in encontrados:
            print(f"Participante {participante[0]}: {participante[1]}, {participante[2]}, {participante[3]} (Suma: {sum(participante[1:]):.2f})")
    else:
        print(f"No hay participantes con una suma de notas igual a {numero}.")

def definir_ganador(matriz):
    """Determina el ganador de una competencia basada en el promedio de las notas de tres jurados para cada participante.
    Si hay un empate en el promedio más alto, el ganador se decide mediante una votación de los tres jurados.


    Args:
        matriz (list of list): Una lista de 5 participantes, donde cada participante es una lista que contiene:
            - `matriz[i][0]`: ID del participante (int)
    """
    # Inicializar el promedio más alto con el promedio del primer participante
    max_promedio = (matriz[0][1] + matriz[0][2] + matriz[0][3]) / 3
    # Buscar el promedio más alto entre todos los participantes
    for i in range(5):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        if promedio > max_promedio:
            # compara el promedio calculado con el maximo promedio actual,Si el promedio del participante i es mayor que el max_promedio calculado hasta ahora, significa que este participante tiene el nuevo promedio más alto.
            max_promedio = promedio
            # si el promedio de i es mayor, actualiza max promedio con este nuevo valor.

    # Encontrar los participantes con el promedio máximo
    ganadores = [] #Inicializa una lista vacía llamada ganadores para almacenar a los participantes que tengan el promedio máximo.
    for i in range(5):
        promedio = (matriz[i][1] + matriz[i][2] + matriz[i][3]) / 3
        if promedio == max_promedio:
            #Verifica si el promedio calculado es igual al max_promedio encontrado en la primera parte de la función. si es así, significa que este participante tiene el promedio más alto.
            
            ganadores.append(matriz[i]) #Si el participante tiene el promedio máximo, se agrega a la lista ganadores.

    if len(ganadores) == 1:
        #Verifica si hay solo un ganador (es decir, solo un participante con el promedio máximo). si la longitud de ganadores es 1, significa que no hubo empate en el promedio más alto.
        print(f"El ganador es el participante {ganadores[0][0]}")
    else:
        # Desempate
        votos = []
        for i in range(3): #recorre la cantidad de jurados
            votos.append(int(input(f"Jurado {i+1}, ¿a quién prefieres como ganador? (Número de participante): "))) #pide a cada jurado que eliga uno de los participantes empatados
        
        contador_votos = [0] * len(ganadores) #crea una lista del mismo tamaño que la lista de ganadores y contiene inicialmente ceros
        for i in range(3):
            for j in range(len(ganadores)): #itera sobre la lista ganadores para comparar el voto de cada jurado con los ids de los participantes
                if ganadores[j][0] == votos[i]:
                    contador_votos[j] += 1
                    #Si el ID del participante ganadores[j][0] coincide con el voto del jurado votos[i], aumenta el contador de votos de ese participante.
        
        max_votos = 0
        index_ganador = -1 #almacena el indice del ganador de la lista ganadores, indica que aun no se ha elegido ningun ganador 
        for i in range(len(contador_votos)): #inicializa un recorrido de todos los votos de los participantes
            if contador_votos[i] > max_votos:
                max_votos = contador_votos[i]
                index_ganador = i
            #Si el participante i tiene más votos que el máximo actual, actualiza el valor de max_votos y asigna el indice del ganador
        
        print(f"El ganador es el participante {ganadores[index_ganador][0]}")


