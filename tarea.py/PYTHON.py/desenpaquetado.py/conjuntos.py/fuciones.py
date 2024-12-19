#creando una funcion simple
def saludar():
    print("hola")
#ejecuntando funcion simple
saludar()
#creando una funcion conpleja
def saludar(numbre,sexo):
    sexo=sexo.lower()
    if (sexo =="mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
     adjetivo = "titan"
    else:
     adjetivo = "crack"
     print(f"hola {numbre},mi {adjetivo} ¿como estas?")
saludar("luci","mujer")

def creando_una_contraseña(num):
   chars="abcdefghj"
   num_entero = str(num)
   num=int(num_entero[0])
   c1=num -2
   c2=num
   c3=num -5
   contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
   return(contraseña)

password = creando_una_contraseña(1)
print(password)

def matematica():
   numeros=3*2
   print (numeros)
matematica()