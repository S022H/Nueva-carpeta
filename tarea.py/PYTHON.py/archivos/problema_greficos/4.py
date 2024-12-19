# Solicitar el año de nacimiento al usuario
anno_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Solicitar el año actual al usuario
anno_actual = int(input("¿En qué año estamos? "))

# Calcular la diferencia de años
edad = anno_actual - anno_nacimiento

# Mostrar la edad del usuario en el año ingresado
print(f"Tienes {edad} años en el año {anno_actual}.")
