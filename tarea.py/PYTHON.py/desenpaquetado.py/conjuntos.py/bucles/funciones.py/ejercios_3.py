#creando una funcion que muestre la serie fumonaci
def fimonaci(num):
    a,b=0,1
    lista_fiminaci=[0]
    for i in range(num):
        if b > num:return lista_fiminaci
        else:
            lista_fiminaci.append(b)
            a,b = b,a+b
resultado=fimonaci(80)
print(resultado)
