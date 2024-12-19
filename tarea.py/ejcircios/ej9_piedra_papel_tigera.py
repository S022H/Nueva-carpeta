import random

def piedra_papel_tijera(jugada_usuario):
    opciones = ["piedra", "papel", "tijera"]
    jugada_maquina = random.choice(opciones)

    if jugada_usuario == jugada_maquina:
        return "¡Empate!"
    elif (jugada_usuario == "piedra" and jugada_maquina == "tijera") or (jugada_usuario == "papel" and jugada_maquina == "piedra") or (jugada_usuario == "tijera" and jugada_maquina == "papel"):
        return "¡Ganaste!"
    else:
        return "La máquina gana."

# Solicita la elección del usuario
eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()

# Llama a la función y muestra el resultado
resultado = piedra_papel_tijera(eleccion_usuario)
print(resultado)
