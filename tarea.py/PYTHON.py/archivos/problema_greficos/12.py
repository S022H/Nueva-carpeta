def eliminar_letras_a(palabra):
    """
    Recibe una palabra y elimina todas las letras 'a'.
    """
    palabra_sin_a = palabra.replace('a', '')
    print(f"Palabra sin letras 'a': {palabra_sin_a}")

# Ejemplo de uso:
mi_palabra = input("Ingresa una palabra: ")
eliminar_letras_a(mi_palabra)

