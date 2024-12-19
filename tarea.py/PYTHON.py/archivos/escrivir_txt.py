with open("archivos\\texto_de_dalto.txt",'w',encoding="UTF-8") as archivo:
 #agregarn linea
# archivo.writelines(["hola como esta gil\n","harassdaw"])
#sobre escriviendo el archivo
#creando un bucle para agregar listas
    archivo.write("\n")
    for i in range(5):
         archivo.write(f"linea {i+1} agregada\n")