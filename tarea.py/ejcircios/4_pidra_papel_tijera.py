import random

def jugar_piedra_papel_tijera():
    """
    Juega al juego de Piedra, papel o tijera contra un programa imposible de ganar.

    Returns:
        None
    """
    opciones = ["R", "P", "T"]
    jugada_usuario = input("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T): ").upper()

    # Validar la entrada del usuario
    if jugada_usuario not in opciones:
        print("Ingresaste una opción inválida. Por favor, elige R, P o T.")
        return

    # Generar la jugada del programa
    jugada_programa = random.choice(opciones)

    # Determinar el resultado
    if jugada_usuario == jugada_programa:
        print(f"{jugada_programa}. ¡Empate!")
    elif (jugada_usuario == "R" and jugada_programa == "T") or (jugada_usuario == "P" and jugada_programa == "R") or (jugada_usuario == "T" and jugada_programa == "P"):
        print(f"{jugada_programa}. ¡Ganaste!")
    else:
        print(f"{jugada_programa}. ¡Te gané!")

# Jugar una partida
jugar_piedra_papel_tijera()
