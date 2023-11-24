import pandas as pd
import numpy as np
from datasets import load_dataset
import csv
import requests

#Parte 6: Automatizando el proceso
def descargar_datos(url):
    
        response = requests.get(url)
        
        if response.status_code == 200:
                return response.text
        else:
            return print(f"Error al descargar los datos. Código de estado: {response.status_code}")
        
def convertir_dataframe(archivo):
       df=pd.DataFrame(archivo)
       return df

def categorizar_en_grupos (df):
       df["Categoria_por_edad"]= pd.cut(df.age,
               bins= [0,12,20,40,60,100] , 
               labels=["niño","adolecente","adulto joven","adulto","adulto mayor"]    )
       return df
def exportar_a_csv(df,filename):
       df.to_csv(filename ,index=False)


def main(url, filename):
    data = descargar_datos(url)
    df = convertir_dataframe(data)
    df = categorizar_en_grupos(df)
    exportar_a_csv(df, filename)     
