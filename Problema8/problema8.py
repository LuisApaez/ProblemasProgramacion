# Solucion problema 8
def sumaMinima(triangulo):

    # Lista de ceros auxiliar
    aux=[0 for i in range(len(triangulo)+1)]

    # Invertimos el orden del triangulo y recorremos cada fila
    for fila in triangulo[::-1]:

        # Recorreremos cada elemento de la fila correspondiente
        for i in range(len(fila)):

            # Asignacion de las sumas
            aux[i]=fila[i]+min(aux[i],aux[i+1])
            
    # el primer elemento es la suma minima
    return aux[0]

c = [[2],[3,4],[6,5,7],[4,1,8,3]]
c2 = [[2],[4,3],[6,5,7],[1,4,8,3]]
d =  [[-1],[2,3],[1,-1,-3]]
print(sumaMinima(c))
