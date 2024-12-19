def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero % 2 == 0:
            print("El número ingresado es par.")
        else:
            print("El número ingresado es impar.")
    except ValueError:
        print("Por favor, ingrese un valor entero válido.")

if __name__ == "__main__":
    main()
