diccionario={
"nombre":'022',
"apellido":'ehc',
"plata":100000,
"hola":'saludo',
}#nombre | clave
claves = diccionario.keys()#devuelve las clave(iterar)

valor_de_plata = diccionario.get("plata")#sepciona el nombre|clave de la diccionario y muetra o muetra none

#elimina todo del diccionario
#diccionario.clear()

#elimina un elemnto de diccionario ejem:diccionario.pop("nombre","etc","etc")se pude eliminar mas de uno
diccionario.pop("nombre")

diccionario_iterble=diccionario.items()#obtine un elemento iterables
print(diccionario_iterble)