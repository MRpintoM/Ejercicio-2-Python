#ejercio # 2
from Poo.EjercicioPar import EjercicioPar
from  Poo.EjercicioImpar import  EjercicioImpar

op= 0

def Menu():
    print("")
    print("                         Hola, Bienvenido al Menu de Opciones                    ")
    print("1. Ejercicios Pares")
    print("2. Ejercicios Impares")
    print("3. Salir")

def SubMenuPar():
    print("                         Hola, Bienvenido a los Ejercicios Pares                         ")
    print("")
    print("1. Leer una secuencia de 30 números y mostrar la suma y el producto de ellos.")
    print("2. Leer dos números y realizar el producto mediante sumas.")
    print("3. Leer una secuencia de números y mostrar su producto, el proceso finalizará cuando el usuario pulse a la tecla F. ")
    print("4. Dado un número mostrar su valor en binario. ")
    print("5. Calcular la media de una secuencia de números, el proceso finalizará cuando el usuario pulse F. ")
    print("6. Leer una secuencia se números y mostrar cuáles de ellos es el mayor y el menor, el proceso finalizará cuando se introduzca un número impar. ")
    print("7. Leer una secuencia de números y mostrar la suma de los 30 números que ocupan posiciones de lectura par. ")
    print("8. Salir")

def SubMenuImpar():
    print("                                           Hola, Bienvenido a los Ejercicios Impares                         ")
    print("")
    print("1. Leer un número y mostrar su tabla de multiplicar")
    print("2. Leer una secuencia de números, hasta que se introduce un número negativo y mostrar la suma de dichos números.")
    print("3. Leer dos números y realizar la división mediante restas mostrando el cociente y el resto.")
    print("4. Lee una secuencia de números y determina cual es el mayor de ellos. ")
    print("5. Generar enteros de 3 en 3 comenzando por 2 hasta el valor máximo menor que calculando la suma de los enteros generados que sean divisibles por 5. ")
    print("6. Generar los N primeros términos de la serie de Fibonacci y mostrarlos por pantalla. El valor N (entero y positivo) deberá ser leído por el teclado. ")
    print("7. Leer una secuencia de números y sumar solo los pares mostrando el resultado del proceso. ")
    print("8. Leer un número y determinar su factorial. ")
    print("9. Salir")


while op !=3: #Menú Principal
    Menu()
    op = int(input("Ingrese una Opción:"))
    print("")
    if (op == 1):
        oppar=0
        while oppar !=8:#SubMenú Ejercicio Pares
            SubMenuPar()
            oppar=int(input("Ingrese una Opción:"))
            if (oppar==1):
                print(" Leer una secuencia de 30 números y mostrar la suma y el producto de ellos.")
                print(EjercicioPar.ejercicioDos())
            if (oppar==2):
                print(" Leer dos números y realizar el producto mediante sumas.")
                print(EjercicioPar.ejercicioCuatro())
            if (oppar==3):
                print(" Leer una secuencia de números y mostrar su producto, el proceso finalizará cuando el usuario pulse a la tecla F. ")
            if (oppar==4):
                print(" Dado un número mostrar su valor en binario. ")
            if (oppar==5):
                print( " Calcular la media de una secuencia de números, el proceso finalizará cuando el usuario pulse F. ")
            if (oppar==6):
                print(" Leer una secuencia se números y mostrar cuáles de ellos es el mayor y el menor, el proceso finalizará cuando se introduzca un número impar. ")
            elif (oppar==7):
                print(" Leer una secuencia de números y mostrar la suma de los 30 números que ocupan posiciones de lectura par. ")

        print("hasta la proxima")
        print("")


    elif (op == 2):
        opimp=0
        while opimp !=9: #SubMenú  Ejercicios Impares
            SubMenuImpar()
            opimp=int(input("ingresa una Opción:"))
            if (opimp == 1):
                print(" Leer un número y mostrar su tabla de multiplicar")
                print(EjercicioImpar.ejercicioUno())
            if (opimp == 2):
                print(" Leer una secuencia de números, hasta que se introduce un número negativo y mostrar la suma de dichos números.")
                print(EjercicioImpar.ejercicioTres())
            if (opimp == 3):
                print(" Leer dos números y realizar la división mediante restas mostrando el cociente y el resto.")
            if (opimp == 4):
                print(" Lee una secuencia de números y determina cual es el mayor de ellos. ")
            if (opimp == 5):
                print(" Generar enteros de 3 en 3 comenzando por 2 hasta el valor máximo menor que calculando la suma de los enteros generados que sean divisibles por 5. ")
            if (opimp == 6):
                print(" Generar los N primeros términos de la serie de Fibonacci y mostrarlos por pantalla. El valor N (entero y positivo) deberá ser leído por el teclado. ")
            if (opimp == 7):
                print(" Leer una secuencia de números y sumar solo los pares mostrando el resultado del proceso. ")
            elif (opimp == 8):
                print("8. Leer un número y determinar su factorial. ")

        print("Hasta la próxima :)")
        print("")


print("Hasta la proxima")
