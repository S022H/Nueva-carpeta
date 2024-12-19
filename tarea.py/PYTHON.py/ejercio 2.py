#le pedimos al usuario que diga barias frases
frases=input("decime la face y tedigo cunto tardarias en decilar:")
#mide la cantidad de frase por la espacios libre
espacio_de_palabras = frases.split(" ")
#usamos len()para ver la cantidad de elementos en el texto en la lista
cantidad_de_palabras=len(espacio_de_palabras)
#te salta una texto si escribis muchu
if cantidad_de_palabras > 120:
    print("para metete el texto en el culo hijo de puta")
#te calcula cuanto tarias vos y cuanto tardaria dalto
print(f'dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundo en decirlo')
print(f'dalto dijo  {cantidad_de_palabras/2*1.3/ 100} kiloioi')
