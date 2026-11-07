# Funcion para pedir los dos numeros
def pedir_numeros():
    numero1 = float(input("Escriba el primer numero: "))
    numero2 = float(input("Escriba el segundo numero: "))

    return numero1, numero2


while True:

    print("==========================")
    print("       CALCULADORA        ")
    print("==========================")

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    eleccion = input("¿Que operacion desea realizar?: ").lower()

    if eleccion == "1" or eleccion == "sumar":
        numero1, numero2 = pedir_numeros()
        total = numero1 + numero2
        print("El resultado es:", total)

    elif eleccion == "2" or eleccion == "restar":
        numero1, numero2 = pedir_numeros()
        total = numero1 - numero2
        print("El resultado es:", total)

    elif eleccion == "3" or eleccion == "multiplicar":
        numero1, numero2 = pedir_numeros()
        total = numero1 * numero2
        print("El resultado es:", total)

    elif eleccion == "4" or eleccion == "dividir":
        numero1, numero2 = pedir_numeros()

        if numero2 != 0:
            total = numero1 / numero2
            print("El resultado es:", total)
        else:
            print("No se puede dividir entre cero")

    elif eleccion == "5" or eleccion == "salir":
        print("Gracias por utilizar la calculadora")
        break

    else:
        print("¡Sea serio! Esa opcion no existe.")
