num=int(input("ingresar primer numeros:"))
num2=int(input("ingresar segundo numeros:"))    
carateres=("caracteres que desea utilisar: sumar,restar,maultiplicar,dividir")                  

opciones=int(input("elige de 1-sumar,2-restar,3-multiplicar,4-dividir:"))

sumar      =num + num2
restar     =num - num2
multiplicar=num * num2
dividir    =num / num2



if 1==sumar:
    print(f"resultado es: {sumar(num,num2)}")
elif restar==2:
    print(f"resultado  es: {restar}")
elif multiplicar==3:
    print(f"resultado  es: {multiplicar}")
elif dividir==4:
    print(f"resultado es: {dividir}")


