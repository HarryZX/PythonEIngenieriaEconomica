def valorPresenteInComp():
    vPresente = input('Ingrese el valor Presente: ')
    interes = input('Ingrese la tasa de interes en decimales: ')
    periodo = input('Ingrese el periodo o tiempo: ')

    vFuturo = vPresente * ((1 + interes) ** periodo)

    print("Valor Futuro",vFuturo)

def valorPresenteInSimp():
    vPresente = input('Ingrese el valor Presente: ')
    interes = input('Ingrese la tasa de interes en decimales: ')
    periodo = input('Ingrese el periodo o tiempo: ')

    vFuturo = vPresente * (1 + interes * periodo)

    print("Valor Futuro: ",vFuturo)

print("*****************************************************")
print("************** CALCULO DEL VALOR FUTURO *************")
print("*****************************************************")
print("*** 1. Formula Interes Simple: F = P(1 + i * n) *****")
print("*** 2. Formula Interes Compuesto: F = P(1 + i)^n ****")
print("*****************************************************")
opc = input('Elije una opcion de calculo de Valor Futuro: ')

if opc == 1:
    valorPresenteInSimp()
elif opc == 2:
    valorPresenteInComp()
