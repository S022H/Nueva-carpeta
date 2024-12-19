def mostrar_anterior_siguiente(numero):
    """
    Recibe un número como argumento y muestra el número anterior y el siguiente.
    """
    anterior = numero - 1
    siguiente = numero + 1
    print(f"El número anterior a {numero} es {anterior}.")
    print(f"El número siguiente a {numero} es {siguiente}.")

# Ejemplo de uso:
numero_ingresado = int(input("Ingresa un número: "))
mostrar_anterior_siguiente(numero_ingresado)
