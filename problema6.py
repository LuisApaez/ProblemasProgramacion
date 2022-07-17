# Problema 6:
# Calcular manualmente la potencia entera de dos numeros x^n, esto es
# calcular la potencia de un número sin recurrir al operador exponencial.
# Además, n debe se un número entero, ya sea positivo o negativo.

def potencia(x,n):
    # Si la potencia es cero, el resultado siempre es uno
    if n == 0:
        return 1
    if x == 0:
    # Si el numero base es cero, la potencia siempre es cero
        return 0
    if n > 0:
    # Caso en que la potencia es mayor a cero
        lista = []
        # Agregamos a la lista copias de x, el numero de copias lo determina n
        for i in range(n):
            lista.append(x)
        # Multiplicamos todos los elementos de la lista, lo cual
        # nos debe dar el resultado de la potencia
        result = 1
        for k in lista:
            result = result * k
        return result
    # Caso en que el exponente es negativo
    else:
        # Hacemos el mismo procedimiento que en el caso positivo, pero con 
        # un exponente positivo n2
        n2 = - n
        lista = []
        for i in range(n2):
            lista.append(x)
        result = 1
        for k in lista:
            result = result * k
        # Por propiedades de los exponentes, el resultado es 1 entre la potencia calculada
        # para n positivo. Esto es x^(-1) = 1/x, o x^(-n) = 1/x^n.
        return 1/result

# --------------

# Prueba
print(potencia(2,5)) 



