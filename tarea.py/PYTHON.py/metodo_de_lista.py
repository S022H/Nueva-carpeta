list=list(["hola",43,121631,15312,123142,667,True,False])

cantidad_de_listas = len(list)#funcionte y dice cuntos elementos hay en la lista

agrego_elemento=list.append("86")#agrega elemto a la lista

list.insert(3,"87")#agrega un elemento en una pocision de asignada
list.extend([4,"4332121"])#agrega varios elementos,se agrega una lista a otra hecha


list.pop(0)#elimina un elemento elegido


list.remove(43)#remueve un elemto por su nombre


#list.clear()#elimina todo de la lista

#no funciona
#list.sort(True) #ordena los elementos de la lista si no son letras



list.reverse()#invierte los elmetos de mayor a menor o la invierte
print(list)