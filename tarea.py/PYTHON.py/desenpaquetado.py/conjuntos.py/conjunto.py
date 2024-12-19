#creando un conjunto
conjunto=set(["dato1","dato2"])
print(conjunto)
#metiendo un conjunto dentro de otro
rama= set(["ramen2","ramen3"])
rama1=frozenset(["ramen1","ramen 2"])
rama2={rama1,"ramen3"}
print(rama2) 

#teoria del conjunto
conjunto1={1,3,5,7}
conjunto2={1,3,7}
#verificacion de sup conjunto
resultado=conjunto2.issubset(conjunto1)
print(resultado)

#verificacion numero en comun y salta false si lo hay
resultado=conjunto2.isdisjoint(conjunto1)
print(resultado )