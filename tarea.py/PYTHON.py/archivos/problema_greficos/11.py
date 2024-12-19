def obtener_primeros_cinco_caracteres(palabra):
    """
    Recibe una palabra y muestra los primeros 5 caracteres.
    """
    primeros_cinco = palabra[:5]
    print(f"Los primeros 5 caracteres de '{palabra}' son: {primeros_cinco}")

# Ejemplo de uso:
mi_palabra = input("Ingresa una palabra: ")
obtener_primeros_cinco_caracteres(mi_palabra)
