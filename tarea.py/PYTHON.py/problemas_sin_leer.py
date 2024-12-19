#cabiar el tipo de datos en una columna

import pandas as pd
df=pd.read_csv("archivos\\archivo.csv")

#convertir en str los datos de una columnas

df['edad']=df['edad'].astype(str)
print(df["edad"])

#usando replace para replasar un nombre,apellido

df['nombre'].replace("dalto","gil",inplace=True)

#print(df['nombre'])

#eleminado la fila con datos faltantes

df=df.dropna()

#eliminado la fila repetidas
df=df.drop_duplicates()

df.to_csv("archivos\\archivo_limpio.csv")