# Define un número (por ejemplo, 6)
numero = int(input("pon un numero:"))

# Verifica si el número es par y menor a 10
es_par_y_menor_a_10 = (numero % 2 == 0) and (numero < 10)

# Imprime el resultado
print(f"¿El número {numero} es par y menor a 10? {es_par_y_menor_a_10}")
