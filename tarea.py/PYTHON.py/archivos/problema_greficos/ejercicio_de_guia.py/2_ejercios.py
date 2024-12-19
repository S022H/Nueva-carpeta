# Define una letra (por ejemplo, 'a')
letra = 'a'

# Verifica si la letra NO es vocal (es decir, no es 'a', 'e', 'i', 'o' o 'u')
no_es_vocal = letra.lower() not in ['a', 'e', 'i', 'o', 'u']

# Imprime el resultado
print(f"¿La letra '{letra}' NO es vocal? {no_es_vocal}")
