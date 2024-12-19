def main():
    # Pedir al usuario que ingrese su nombre y apellido
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")

    # Concatenar apellido y nombre en el formato "Apellido, Nombre"
    nombre_completo = f"{apellido}, {nombre}"

    # Imprimir el resultado
    print(f"El nombre completo en formato 'Apellido, Nombre' es: {nombre_completo}")

if __name__ == "__main__":
    main()
