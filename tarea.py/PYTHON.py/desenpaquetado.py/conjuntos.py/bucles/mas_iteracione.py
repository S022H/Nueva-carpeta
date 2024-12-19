print("0-------------------------------------------------------")
frutas=["banana","manzana","durasno","granada","ciruela","pera"]
for fruta in frutas:#interumpiedo que se coma una manzana con continue
    if fruta == 'manzana':
      continue
    print(f'me  voy a comer una {fruta}')
print("1 ------------------------------------------------------")
for fruta in frutas:#interumpiedo que se coma una manzana con continue
    if fruta == 'durasno':
      break
    print(f'me  voy a comer una {fruta}')
print("2 ------------------------------------------------------")
numeros=(1,2,3,4,5,6,7,8,9,0,)
for numero in numeros:
   if numero == 9:
      continue
   print(f'voy a contar hasta {numero}')

print("3 ------------------------------------------------------")
numeros=(1,2,3,4,5,6,7,8,9,0,)
for numero in numeros:
   if numero == 4:
      break
   print(f'voy a contar hasta {numero}')
print("4-------------------------------------------------------")
#for en una sola linea duplicados
numeros_duplicados=[x**2 for x in numeros]
print(numeros_duplicados)

#recorer una cadena de texto(iterar)
cadena=("hola ezequiel")
for letra in cadena:
   print(letra)



