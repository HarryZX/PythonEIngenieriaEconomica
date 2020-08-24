def calculoInversion():
    print("\n***** Calculo de los intereses acumulados en un determinado tiempo *****\n")
    inversion = input('Ingrese la cantidad a inertir: ')
    interes = input('Ingrese la tasa de interes en decimales: ')
    periodo = input('Ingrese los anios: ')

    # Variables para la tabla
    inormal = inversion * interes
    iacum = 0
    ivaluado = 0
    iefectiva = 0
    print("----------------------------------------------------------------------")
    print("|\tanio\t|\tcapital\t|\tinteres\t| interes acumulado |")
    print("----------------------------------------------------------------------")
    for x in xrange(1,periodo+1):
        iefectiva = inversion + iacum
        ivaluado = iefectiva * interes
        iacum = iacum + ivaluado
        print("|\t" + str(x) + "\t|\t" + str(round(iefectiva)) + "\t|\t" + str(round(ivaluado)) + "\t|\t" + str(round(iacum)) + "\t|")

    recuperado = inversion * ((1 + interes) ** periodo)

    print("\nValor Futuro de la inversion: $" + str(recuperado))

def duplicarInversion():
    print("* EN PROCESO *")

print("**********************************************************")
print("************** CALCULO DEL INTERES COMPUESTO *************")
print("**********************************************************")
print("**** 1. Calcular el valor futuro de una inversion ********")
print("**** 2. Calculo de los anios para duplicar una inversion *")
print("**********************************************************")
opc = input('Elije una opcion para el calculo de la inversion: ')

if opc == 1:
    calculoInversion()
elif opc == 2:
    duplicarInversion()
