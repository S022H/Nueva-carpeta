#creando una funcion que nos devuelve los numeros primos entre 0 y el que elegimos
#creando una funcion que verifique si en primo
#verificado que los numeros pasado no fuedan dividirse por ningun numero entre 2 y ese mismo numero
def es_primos(num):
    #si es divicible terminara en bucle y retornara false
    for i in range(2,num-1):
        if num%i==0: return False
    #si termina el bucle temina segnifica que es primos
    return True
#creando una funcion que retorna una lista con todos los primos
def primos_hasta(num):
    #creando una lista
    primos = []
    for i in range(1,num+1):
        #verificamos que sea primo
        resultado = es_primos(i)
        #lo agregamos a la lista
        if resultado == True:primos.append(i)
    #devolvemos la lista
    return primos
#creamos el resultado llamado a la funcion y lo mostramos 
resultado=primos_hasta(13)
print(resultado)