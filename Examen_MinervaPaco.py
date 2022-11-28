
num1 = 0
num2 = 0
suma = 0
opcion = 0

def Menu():
    print("MENÚ")
    print("1:Sumar")
    print("2:Salir")
    print("\n")


def Suma(num1,num2):
    suma = num1+num2
    return(suma)


while (opcion!=2):    
    print(Menu())
    opcion = int(input("Elige una opción:\n"))

    if (opcion==1):
        try:
            num1 = int(input("Dime un número:\n"))
            num2 = int(input("Dime otro número:\n"))
            print(Suma(num1,num2))
        except:
            print("Tienes que introducir dos números")
            print("******")

print("Has salido")