# Solucion del problema 3

def div(dividend, divisor):
    if divisor != 0:
        if divisor < 0:
            div_pos = - divisor
        else:
            div_pos = divisor
        if dividend < 0:
            divid_pos = - dividend
        else:
            divid_pos = dividend
        def cociente(dividend, divisor):
            contador = 0
            while dividend >= divisor:
                dividend -= divisor
                contador += 1
            return contador, dividend
        residuo_aument = int(str(cociente(divid_pos,div_pos)[1]) + '0')
        if cociente(residuo_aument, div_pos)[0] >= 5:
            x = cociente(divid_pos, div_pos)[0] + 1
        else:
            x = cociente(divid_pos, div_pos)[0]
        if (divisor > 0 and dividend > 0) or (divisor<0 and dividend <0):
            return x
        elif dividend < 0  or divisor <0:
            return -x
    else:
        return 

# Prueba de la funcion
print(div(-11,3))