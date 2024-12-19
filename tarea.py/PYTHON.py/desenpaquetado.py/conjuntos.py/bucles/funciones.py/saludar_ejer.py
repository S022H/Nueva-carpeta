#importamos modulo de metodo
import modulos
saludo=modulos.saludar("lucas")
print(saludo)

#importamos la funcion de un modulo
from modulos import saludar,saludar_raro
#creamo las variables
saludo=saludar("eze")
saludo_raro=saludar_raro("ale")
#mostramos los resultado
print(saludo)
print(saludo_raro)