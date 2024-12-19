#creo una lista
animales =["perro","ola","loro","asta"] 
#muestra la lista de animales
for animal in animales:
    print(f'ahora la variable animal es {animal}')

#numero multiplicados puede renplasase por una tubla
numeros=[2,3,4,18]
for numero in numeros:
    resultado=numero*2
    print(resultado)

#usando el for
for numero,animal in zip(numeros,animales):
 print(f"recoriendo lista 1:{numero}")
 print(f"recoriendo lista 2:{animal}")

#forma no corepta de recorer un lista en indice
for nunn in range(len(numeros)):

 # print(numeros[num])
#forma corepta de recorrer una lista en indice
 for num in enumerate(numeros):
   indice=num[0]
   valor=num[1]
   print(f'el indice es : {indice} y el vaor es : {valor}')

#usando el for / else
for numero in numeros:
   print(f"ejecuntando el ultumo valor actual: {numero}")
else:
    print("bucle termino")
