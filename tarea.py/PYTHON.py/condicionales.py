#condicionales
edad=18
if  edad <=19:
 print("podes pasa")
#nota necesita un espacio para que no forme el mismo codigo y funcione bien
else:
 print("no podes pasar")

#if debajo d otro if esmpara poner otra condicion 
años=10
amigos=5
if años >= 18:
 if  amigos < 6:
     print("adulto") 
#elif significa es caso cotrario seria para que se ejecute si la condicion anterio no se cunplio
elif años < 16:
 print("adolecente")

#ejemplo:condicionales
dinero=10000
impustos=100
#condicion para que se jecute el codigo
if dinero <= 10000:
  if impustos >= 10:
    print("estas bien")
#de lo contrario se ejecuta este codigo
else:
 print("estas mal")

