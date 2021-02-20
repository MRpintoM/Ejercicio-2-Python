class EjercicioImpar():

    def ejercicioUno():
        dato=int(input("Ingrese un Número:"))
        for i in range(12):
            contador=dato*i
            print("el Número a multiplicar es:" ,dato, " x " ,i, " = ",contador)

    def ejercicioTres():
        num1=1
        residuo = 0
        while (num1>0):
            num1 =int(input("Escriba un Número:"))
            if (num1 > 0):
                print(f"El resultado es: {num1}")
                residuo = residuo + num1
                print(residuo)
            else:
                print("Usted a ingresado un número negativo ")
                print("Fin del programa")

