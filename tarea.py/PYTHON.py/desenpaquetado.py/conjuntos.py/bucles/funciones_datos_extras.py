def frase (nombre,apellido,adjetivo):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultado = frase(adjetivo= "genio",nombre="eze",apellido="caballero")
print(frase_resultado)

def informasion(saludo,nombre,apellido):
    return f'{saludo} {nombre} {apellido}'
presentacion=informasion(saludo="hola",nombre="ezequiel",apellido="caballero")
print(presentacion)