def contar_letras(palabra):
    """
    Recibe una palabra como argumento y muestra la cantidad de letras.
    """
    cantidad_letras = len(palabra)
    print(f"La palabra '{palabra}' tiene {cantidad_letras} letras.")

# Ejemplo de uso:
mi_palabra = input("Ingresa una palabra: ")
contar_letras(mi_palabra)
