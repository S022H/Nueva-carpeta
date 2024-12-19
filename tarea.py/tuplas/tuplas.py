#se agrupan entre parentecis
#no se pueden modificar
#agrupar datos que tengan relacion ejemplos:
contenido=("ezequiel",18),("jorge",24)
colores=("pares","roja",),("banana","amarilo")

#lista con tuplas
#podemos hacer como una lista ejemplo
jugadores=[("messi",10),("pele",8),("rolnaldo",7)]
# print(jugadore[0])

#usando for para iterar
for listando_jugadores in jugadores:
#print(f"lista de jugadores:{listando_jugadores}")
    

#usando max,min para save el minimo y el maximo
 def puntacion(puntos):
    max_puntos=max(puntos)#vemos el mejor resultado
    min_puntos=min(puntos)#el peor resultado
    return max_puntos,min_puntos 
datos=[12,44,76]
resultado=puntacion(datos)
max_resultado=resultado[0]
min_resultado=resultado[1]

#print(f"mejor resulatdo: {max_resultado}")
#print(f"resultado mas vajo: {min_resultado}")

#hacemos un lista vacia y con append elegimos los indice para la lista team
#lo restornamos
#cabiamos leo por jorje y lo mostramos
def team_red(player):
    team=[]
    team.append(player[0])
    team.append(player[2])
    return team
player=["leo","never","lader","merde"]
team=team_red(player)
team[0]="jorje"
print(team)

