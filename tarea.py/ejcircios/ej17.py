
    
def calculadora(operador,a,b):
    if operador=="+":
        print(a+b)
    elif operador=="-":
        print(a-b)
    elif operador=="*":
        print(a*b)
    elif operador=="/":
        print(a/b)
    else:
        print("ERROR!!")

resultado=calculadora("*",4,4)
print(resultado)