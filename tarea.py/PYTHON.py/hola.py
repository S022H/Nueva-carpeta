#definiendo variables
numero="22  " 
#concantenar con f+"string"=PASA todo a texto
datos= f"hola {numero} "
#operadores de pertenencia in y in not para saber si un dato esta o no
print( "22" in datos)
print( "22" not in datos)
#concatenacio
print(datos+numero)
print(datos + datos + datos)
#lista de elementos
list=["hola","jose","romero","jaimito","true","in",]
print(list [3])
#edicion de lista
list[3]="sabado"
#nose puede editar es fijo pero puede se replasado por otro elemeto
tuple=["hola","jose","romero","jaimito","true","in",]
print(tuple [3])
#elementos desordenado pero puede se replasado por otro elemeto no muestra duplicados
conjunto={"hola","jose","romero","jaimito","true","in","jose",}
print(conjunto )
diccionario = {  
    'hola': "saludo",
    'leo' :"tonto",
    }
print(diccionario)
