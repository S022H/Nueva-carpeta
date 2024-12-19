print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")

cadena_original = "Python"
cadena_invertida = cadena_original[::-1]
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")

def invertir_cadena(cadena):
    cadena_invertida = ""
    for char in cadena:
        cadena_invertida = char + cadena_invertida
    return cadena_invertida

cadena_original = "Guru999"
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {invertir_cadena(cadena_original)}")

print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")


