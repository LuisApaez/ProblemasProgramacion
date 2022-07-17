# Solucion problema 4

def isValid(s):
    lista = []
    auxiliar = []
    for i in s:
        if i in ('(', '[', '{'):
            lista.append(i)
        elif i in (')', ']', '}'):
            auxiliar.append(i)
            if len(lista) == 0:
                print(False)
            else:
                if i == ')' and  lista[-1] == '(':
                    lista.pop()
                    auxiliar.pop()
                elif i == ']' and  lista[-1] == '[':
                    lista.pop()
                    auxiliar.pop()
                elif i == '}' and  lista[-1] == '{':
                    lista.pop()
                    auxiliar.pop()
    if not lista and not auxiliar:
        print(True)
    else:
        print(False)

# Cadenas prueba
s1 = '([}]})'
s3 = '(]'
s4 = '{}()()[]()'
s5 = '{()[(())]}'
s6 = '(})[()]{'
s7 = '{{}}'
s8 = '(}{}{)'
s9 = '()[]{}'
s10 = '([)]'

# Prueba de la funcion
isValid(s1)
