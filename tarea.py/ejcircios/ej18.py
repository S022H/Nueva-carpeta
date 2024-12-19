#replasar
def renplace_lista(lista1,lista2):
    lista1[0]=lista2
    return lista1
lista1=["u","d","t","c"]
lista1=renplace_lista(lista1,"uno")    
print(lista1)

print("__________________________________________________")
#usado len en una funcion
def num_lista(conparador):
    print(len(conparador))
comparador=["hola","sabado","lunes"]
num_lista(comparador)    

print("__________________________________________________")
#cotraseña
def caja_negra(contraseña):
   if  contraseña==3004:
       print("open")
   else:
       print("contasena incorreta")
caja_negra(3004)
#len en una funcion
print("____________________________________________________")

def conparado(num):
    print(len(num)>4)
num=["j","l","e","na"]
conparado(num)
    
    