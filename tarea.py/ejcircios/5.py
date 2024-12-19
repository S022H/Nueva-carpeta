def calcular_diferencia_para_llegar_a_limite(num1, num2, limite):
    """
    Calcula la diferencia necesaria para llegar a un límite dado.

    Args:
        num1 (int): Primer número.
        num2 (int): Segundo número.
        limite (int): Límite deseado.

    Returns:
        int: Diferencia necesaria para llegar al límite.
    """
    suma = num1 + num2
    if suma < limite:
        return limite - suma
    else:
        return 0

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    limite = int(input("Ingrese el límite deseado: "))

    diferencia = calcular_diferencia_para_llegar_a_limite(num1, num2, limite)

    if diferencia > 0:
        print(f"Faltan {diferencia} para llegar a {limite}.")
    else:
        print(f"Llega a {limite}.")

if __name__ == "__main__":
    main()
