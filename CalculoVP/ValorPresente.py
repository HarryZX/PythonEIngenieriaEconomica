def valorPresenteInSimp():
    vFuturo = input('Ingrese la cantidad del valor futuro: ')
    interes = input('Ingrese la tasa de interes en decimal: ')
    periodo = input('Ingrese el periodo o tiempo: ')
    
    vPresente = vFuturo / (1 + interes * periodo)

    print("El valor presente es: ", vPresente)

def valorPresenteInComp():
    vFuturo = input('Ingrese la cantidad del valor futuro: ')
    interes = input('Ingrese la tasa de interes en decimales: ')
    periodo = input('Ingrese el periodo o tiempo: ')

    vPresente = vFuturo / ((1 + interes) ** periodo)

    print("El valor presente es: ", vPresente)

print("*************************************************")
print("********** CALCULO DEL VALOR PRESENTE ***********")
print("** 1. Formula Interes Simple: P = F/(1 + i*n) ***")
print("** 2. Formula Interes Compuesto: P = F/(1+i)^n **")
print("*************************************************")
opc = input('Elije un calculo del valor presente: ')

if opc == 1:
    valorPresenteInSimp()
elif opc == 2:
    valorPresenteInComp()
