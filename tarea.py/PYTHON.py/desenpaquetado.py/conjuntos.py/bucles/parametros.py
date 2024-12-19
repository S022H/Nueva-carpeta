#forma no optima
#def suma(lista):
 #   numeros_sumado=0
  #  for numeros in lista:
   #     numeros_sumado=numeros_sumado + numeros
    #return numeros_sumado
#resultado=suma ([5,3,1,2,3,23,4])
#print(resultado)    

#utilizamos el parametro args
def suma (nombre,*numeros):
    return  f"{nombre}, la suma de estos numero es: {sum(numeros)}"

resumatado = suma("eze",4,2,34,3)
print(resumatado)