import random
juego="piedra","papel","tijera"
jugada_maquina = random.choice(juego)
usuario=str(input("eligir jugada piedra,papel o tijera:"))

if usuario == "piedra" and jugada_maquina=="tijera" or usuario == "papel" and jugada_maquina=="piedra" or usuario=="tijera" and jugada_maquina=="papel" :
    print("!!GANADOR!!")
    
elif jugada_maquina=="piedra" and usuario== "piedra" or jugada_maquina=="papel" and usuario=="papel" or jugada_maquina=="tijera" and usuario=="tijera":  
    print("!!EMPATE!!")
else:
    print("!!PERDEDOR!!")