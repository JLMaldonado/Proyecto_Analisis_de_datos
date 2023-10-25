import pandas as pd
import numpy as np
import csv
import requests
#Parte 5: Limpieza y preparación de datos
df=pd.read_csv("archivos_clinicos.csv")

def Limpieza_de_datos(df):
#Verificar que no existan valores faltantes
    df_limpio=df.dropna()

#Verificar que no existan filas repetidas
    df_sin_duplicados=df_limpio.drop_duplicates()

#Verificar si existen valores atípicos y eliminarlos
    df= pd.DataFrame(df_sin_duplicados)

# Calcular el rango intercuartil (IQR)
    Q1 = df.quantile(0.25)  
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
# Definir los límites para detectar valores atípicos
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

# Filtrar los valores atípicos
    df_cleaned = df[(df >= lower_bound) & (df <= upper_bound)]
    df_cleaned= df_cleaned.dropna()
# Resultado

#Crear una columna que categorice por edades
    df=pd.DataFrame(df_cleaned)

    df["Categoria_por_edad"]= pd.cut(df.age,
               bins= [0,12,20,40,60,100] , 
               labels=["niño","adolecente","adulto joven","adulto","adulto mayor"]    )

    df.to_csv("Datos_categorizados_por_edad.cvs" ,index=False)
    return df
c=Limpieza_de_datos(df)