# 2 lista una con nombre y otra con apellido
nombres=["lucas","eze","leo","cero","german","juan"]
apellidos=["dalto","caballero","isma","dos","garmendia","perez"]
#registramo en un archivo de texto de forma optima
with open("nombres_y_archivos.txt","w") as arch:
 arch.writelines("los datos son:\n\n")
 [arch.writelines(f"nombre: {n}\napellido: {a}\n----------------------\n") for n,a in zip(nombres,apellidos)]