# Solucion del problema 1

# Funcion:
def conversor(roman):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num=0
    continuar = []
    for i in range(len(roman)):
        if i in continuar:
            continue
        if i < len(roman)-1:
            if dic[roman[i]] < dic[roman[i+1]]:
                 num += dic[roman[i+1]] - dic[roman[i]]
                 continuar.append(i+1)
            else:
                num += dic[roman[i]]
        else:
            num += dic[roman[i]]
    return num
    
# Prueba
print(conversor('MCMXCIX'))