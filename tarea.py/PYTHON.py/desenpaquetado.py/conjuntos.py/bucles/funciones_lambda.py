#ejemplo 
def multiplicar_por_dos(x):
    return x*2

#creando una funcion lanbda que multiplica por dos
multiplica_por_dos=lambda x:x*2

#creando una funcion que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
#usando filter con una funcion comun
numeros=[1,2,3,4,5,6,7,8,9,0]
numeros_pares= filter(es_par,numeros)
print(list(numeros_pares))

#creando lo mismo pero con labda
numeros_pares= filter(lambda numero:numero %2 == 0,numeros)
print(list(numeros_pares))