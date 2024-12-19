#lsita con dict()
diccinario=dict(nombre="lucas",apellido="dalto")
#las lista no pueden ser claves Y usar frozenset para meter conjuntos
diccinario={frozenset(["nombre","apellido"])}
#creando un diccionario con fromkeys
diccinario=dict.fromkeys(["nombre","apellido"])
print(diccinario)
