def es_multiplo(numero, multiplo):
    return numero % multiplo == 0

# Ejemplo: ¿Es 9 múltiplo de 3?
if es_multiplo(3, 3):
    print("Sí es múltiplo")
else:
    print("No es múltiplo")
