archivo_sin_leer=open("archivos\\texto_de_dalto.txt",encoding="UTF-8")
#leer archivos completos
archivo=archivo_sin_leer.read()
#leer una sola linea
linea=archivo_sin_leer.readline(1)
#leer linea por linea
linea_1=archivo_sin_leer.readlines()
#cerrar archivo
archivo_sin_leer.close()
print(linea_1)