#metodos son funciones aplicadas a opjetos primera letra en MAYUCULA.
#dir ejemplo de funcion
hola="saludo"
# print(dir(hola))
#metodo= DATO.METODO()
cadena = "aijsonasf"
Mayucula= cadena.upper()#tranforma en MAYUCULA
minuscula=cadena.lower()#tranforma en minucula
primera_mayucula=cadena.capitalize()#Primera Letra En Mayucula

busqueda_en_cadena=cadena.find("o")#buqueda en otras cadena sino encuetra mustra -1
busqueda_en_cadena=cadena.index("o")#buqueda en otras cadena sino encuetra mustra epxecion

numerico="lamamamaammmammamamamamamamamamamamammaammamaammdadadasfr"
es_numeros=numerico.isnumeric()#si hay numeros da true sino es false
es_alfanumerico=numerico.isalpha()#pone true si hay alfanumericos sino false

cuenta_las_coisidencia=numerico.count("lama")#encuentra la coisidencia

#metodo=metodo(dato)
cuenta_caracter=len(numerico) #cuenta caracteres

cadena_empiza=numerico.startswith("l")#tedice true si una cadena en piza con la palabra o letra que pusimos
cadana_termina=numerico.endswith("m")#tedice true si una cadena en termina con la palabra o letra que pusimos

#metodo=dato.metodo("origina","nuevo")
renplaso_cadena=numerico.replace("lam","lamama")#replasa el dato o texto de una cadena si encuenta la coinciden que pucimos
#metodo=metotodo.solit("texto")
cadena_separada=numerico.split("a")#crea una lista con el texto por la palabra o letra asignada
print(cadena_separada[0])