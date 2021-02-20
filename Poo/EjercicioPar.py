class EjercicioPar():
   def ejercicioDos():
        num1=[]
        limite=30
        suma=0
        producto=1
        while (limite>0):
            numero= int(input("Ingrese los Números:"))
            num1.append(numero)
            limite = limite -1

            for i in num1:
                suma = suma + i
            for i in num1:
                producto = producto * i

            print(f"La suma de los Número es:{suma}")
            print(f"El Producto de los Número es:{producto}")

   def ejercicioCuatro():
        num1=int(input("Ingrese el Primer Número:"))
        num2=int(input("Ingrese el Segundo Número:"))
        producto=0
        dato=num1+1
        for i in range(1,dato):
            producto = producto - num2
            print("El resultado del producto es:" ,producto)
