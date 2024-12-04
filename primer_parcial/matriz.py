def inicializar_matriz():
    """Funcion para inicializar una matriz que representa 5 participiantes

    Returns:
        la matriz, cada uno con un ID diferente y tres notas inicializadas en 0.
    """
    matriz = [] #creacion de la matriz vacia
    for i in range(5): #se itera 5 veces del 0 al 4
                matriz.append([i + 1, 0, 0, 0])  
    return matriz