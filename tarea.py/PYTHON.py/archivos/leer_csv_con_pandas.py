import pandas as pd 
#usando la funcion read_csv para leer el archivo
df= pd.read_csv("archivos\\archivo.csv")
df2= pd.read_csv("archivos\\archivo.csv")
#obteniendo los datos de la columna nombre
#print(df["nombre"])

df_ordenado_acendente=df.sort_values("edad")


df_ordenado_decendente=df.sort_values("edad",ascending=False)

df_concatenado=pd.concat([df,df2])


prime_fila=df.head(1)

ultimas_filas=df.tail(3)


#acediendo la catidad de columnas con shape
filas_totales,columnas_totales=df.shape


#obteniendo data estadistica del dataframer
df_info=df.describe()

#acediendo a un elemento especifico del df con loc
elemento_especifico_loc=df.loc[2,"edad"]

##acediendo a un elemento especifico del df con iloc
elemento_especifico_iloc=df.iloc[2,2]

#acediendo a la fila de una columnas
apellido=df.iloc[:,1]
#acdiendo a toda la columna con loc,iloc
fila_3_loc=df.loc[2,:]

#acediendo a columnas mayores a 30
mayore_que_30=df.loc[df["edad"]>30,:]
print(mayore_que_30)
