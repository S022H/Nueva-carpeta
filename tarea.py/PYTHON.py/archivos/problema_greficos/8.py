def obtener_resto_y_cociente(dividendo, divisor):
    """
    Recibe un dividendo (entero) y un divisor (entero distinto de cero).
    Devuelve el resto y el cociente como una tupla.
    """
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")

    cociente = dividendo // divisor
    resto = dividendo % divisor

    return (resto, cociente)

# Ejemplo de uso:
try:
    num1 = int(input("Ingresa un dividendo (entero): "))
    num2 = int(input("Ingresa un divisor (entero distinto de cero): "))
    resultado = obtener_resto_y_cociente(num1, num2)
    print(f"Resto: {resultado[0]}, Cociente: {resultado[1]}")
except ValueError:
    print("Por favor, ingresa valores enteros válidos.")
