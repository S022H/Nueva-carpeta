#falto el profe y los pibes van a armar la clase

#pedir el nombre y edad de los compañeros que vinieron a la clase
def obtener_compañeros(cantidad_de_compañeros): 
    #creando un lista de copañeros
    compañeros = []
    for i in range(cantidad_de_compañeros):
        #ejecuntado for para pedir informacio sobre los compañero
        nombre = input("ingrese el nombre de los copañero: ")
        edad = int(input("ingrese la edad de los compañero: "))
        compañero = (nombre,edad)
        #agregando informacio a la lista
        compañeros.append(compañero)
    #orgendo sugun su edad
    compañeros.sort(key = lambda x:x[1])
    #compañeros [x] devuelven una tupla con [nombre,edad] y despues accedemos al nombre
    #para definir al asistente y el profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #retornamos una tupla
    return asistente,profesor
#desenpaque tamos lo que nos retorna la funcion
asistente,profesor=obtener_compañeros(5)

print(f"el profesor es: {profesor} y su asitente es {asistente}")
