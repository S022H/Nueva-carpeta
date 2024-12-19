def unir_string_entero(string_valor, entero_valor):
    """
    Recibe un string y un entero, y los une dentro de un nuevo string.
    """
    resultado = string_valor + str(entero_valor)
    return resultado

# Ejemplo de uso:
mi_string = "Hola, el número es: "
mi_entero = 42
resultado_final = unir_string_entero(mi_string, mi_entero)
print(resultado_final)
