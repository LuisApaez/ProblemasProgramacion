# Problema 7:
# Tringulo de pascal.
# Dado un número entero mayor o igual a 1, retornar la fila
# que representa la fila n del triángulo de pascal.

def pascal(n):
    # Fila 1
    if n == 1:
        return [[1]]
    # Fila 2
    if n == 2:
        return [[1],[1,1]]
    else:
        # Fila n
        # Accedemos a la fila anterior
        aux = pascal(n-1)
        # Creamos una lista auxiliar para construir la fila n
        aux2 = [0,1]
        # Sumamos las entradas de la fila anterior en un rango indicado
        for i in range(0, len(aux[-1])-1):
            valor = aux[-1][i] + aux[-1][i+1]
            # Agregamos el valor a la lista auxiliar
            aux2.append(valor)
        # Agregamos el último cero de la fila
        aux2 += [1]
        # Agregamos la fila n a la lista de las filas anteriores
        aux.append(aux2[1:])
        return aux

# Prubas
print(pascal(4))
print(pascal(5))
print(pascal(6))