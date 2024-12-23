def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "¡Error! No se puede dividir entre cero."

def menu():
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Selecciona una opción (1/2/3/4/5): "))
        if opcion == 5:
            print("¡Hasta luego!")
            break
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if opcion == 1:
            print(f"Resultado de la suma: {suma(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado de la resta: {resta(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado de la multiplicación: {multiplicacion(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado de la división: {division(num1, num2)}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

