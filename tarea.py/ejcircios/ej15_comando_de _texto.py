                                             #METODOS PARA CADENA O TEXTO

#poner en MAYUCULA
texto="hola me llamo juan de la mar"
texto=texto.upper()

#poner en minuscula
texto1="hola me llamo juan de la mar"
texto1=texto1.lower()

#renplasar
texto2="hola me llamo juan de la mar"
texto2=texto2.replace(" ","---")

#elimina los espacios vacio de una cadena al principio y al final
texto3="hola,me llamo juan de la mar"
texto3=texto3.strip()

#crea diferentes textos de uno solo
texto4=texto3.split()

#busca si esta hay concidencia en otra cadena y devuelve el indice
busqueda=texto2.find("hola")

#lo mismo pero devuelve una execion si no encuentra el resultado
busqueda=texto2.index("hola")

#verifica si es numerico devoviendo true o false
numeric=texto2.isnumeric()

#verifica si es alfa numerico (numeros y letras) devoviendo true o false

alfa_numeric=texto2.isalpha()

#cuantas veces encuentra coicidencias
busqueda_considencia=texto2.count("hola")


print()




