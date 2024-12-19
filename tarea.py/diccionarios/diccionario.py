#dicionario ejemplo
#para no llamar por el indice podemo poner una palabra clavea
datos={
    10:"messi",
    7:"cristiano",
    "name":"jorge",
    "usuario":"jorgeriquelme123@gmail.com",
    "passwort":"jorge123"
}
datos["usuario"]

print("----------------------------------------------------")

#almacenado informacion en una variable
data_usuario=datos["usuario"]
print(data_usuario)

print("----------------------------------------------------")

for dato in datos:
    print(datos[dato])
    
print("----------------------------------------------------")

#actaulizando el diccionario
compras={"manzana":True,
         "azucar":False,
         "arroz":False
          }
compras["azucar"]=True
print(compras)

print("----------------------------------------------------")

#usando tupla en un diccionario
lugares={
    "1ro":("jorge",45),
    "2do":("maria",40),
    "3ro":("vistor",38)

}
print(lugares["1ro"])

print("----------------------------------------------------")

#agragando clave y valor al diccionario
lugares["4to"]=("santiago",38)
print(lugares)

print("----------------------------------------------------")
#con in podemos conprobar si la clve esta presente si esta true no esta false
#ejemplo

print("1ro" in lugares)
print("5to" in lugares)

print("----------------------------------------------------")
#podemos eliminar cosa como en una lista
#y almacenarla
datos1={
    10:"messi",
    7:"cristiano",
    "name":"jorge",
    "usuario":"jorgeriquelme123@gmail.com",
    "passwort":"jorge123"
}

print("----------------------------------------------------")
#es bueno ordenar que verifique ante de eliminar la clave para evitar errores

if "name" in datos1:
    datos1.pop("name")
print(datos1)