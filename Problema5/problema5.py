# Problema 5:
# Crear una función que calcule la raiz cuadrada de un número, sin recurrir
# al operador exponencial. Esta funcion debe arrojar solo numeros enteros, por lo cual
# se debe redondear al menors entero mas cercano. Ejemplo, 2.7 se redondea a 2

# solucion:
def raiz(x):
    # Si el numero es cero, la raiz es cero
	if x == 0:
		return 0
	elif x == 1:
    # Si el numero es uno, la raiz es uno		
		return 1
	# Si el numero es negativo, la raiz no existe
	elif x < 0:
		return "Error"
	else:
		# En cualquier otro caso
		# Creamos una lista vacia
		push = []
		# Realizaremos multiplicaciones de un numero consigo mismo
		# comenzando por el 2 (2*2) hasta el numero en cuestion (x*x)
		for i in range(2,x):
			y = i * i
			# Si el producto anterior es menor o igual al numero dado
			# entonces lo agregamos a la lista. Asi, agregaremos todos los cuadrados
			# hasta llegar a un cuadrado menor a x
			if y <= x:
				push.append(i)
			# Si el cuadrado es mayor a x lo descartamos y el bucle for termina
			else:
				break
		# El ultimo cuadrado guardado en la lista es el mas cercano a x, por lo cual
		# es el mas proximo a ser su raiz cuadrada
		return push[-1]
print(raiz(1))

