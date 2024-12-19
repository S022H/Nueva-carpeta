a=int(input("pon un numero:"))
b=int(input("pon un numero:"))
sumar=a+b
restar=a-b
opearador=input("""pon un opearador:
 a sumar:
 b retar:""")
if opearador=="a":
    print(sumar)
elif opearador=="b":
    print(restar)
else:
    print("ERROR")