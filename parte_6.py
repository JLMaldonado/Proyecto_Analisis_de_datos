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
       