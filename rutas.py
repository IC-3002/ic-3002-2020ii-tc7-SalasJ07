def encontrar_ruta(C): 
    Filas = len(C)          #Filas
    Columnas = len(C[0])    #Columnas
    R = [[0 for j in range(Columnas)]for i in range(Filas)]  #Crea nueva matriz del tamano de C
    Filas -=1
    Columnas-=1
    if ruta_backtrack(C, 0, 0, Filas, Columnas, R) == False: #Primera llamda recursiva
        R = [] 
        return R        #Retorna R vacio si no encontro camino   
    return R            #Retorna nueva matriz con el camino encontrado
      

#Funcion de validacion
def esViable(Filas, Columnas, C, fila, col):     
    if fila <= Filas and col <= Columnas and C[fila][col] == 0: 
        return True  
    return False


#Funcion recursiva
def ruta_backtrack(C, fila, col, Filas, Columnas, R):       
    if fila == Filas and col == Columnas and C[fila][col] == 0: 
        R[fila][col] = 1
        return True

    #Valida si puede moverse a la siguiente casilla
    if esViable(Filas, Columnas, C, fila, col) == True:
        R[fila][col] = 1         

        try:         
            #Busca camino moviendose hacia abajo
            if ruta_backtrack(C, fila + 1, col, Filas, Columnas, R) == True:
                return True

            #Busca camino moviendose a la derecha 
            if ruta_backtrack(C, fila, col + 1, Filas, Columnas, R) == True: 
                return True
        
            #Si no encuentra camino, realiza backtrack 
            R[fila][col] = 0
            return False
        except RecursionError as e:
            R = []
            return R
